import siliconcompiler

from siliconcompiler.tools.openroad import rcx_bench
from siliconcompiler.tools.openroad import rcx_extract
from siliconcompiler.tools.builtin import nop


############################################################################
# DOCS
############################################################################
def make_docs(chip):
    return setup(chip, corners=5)


###########################################################################
# Flowgraph Setup
############################################################################
def setup(chip, extraction_task=None, corners=1):
    '''
    Flow to generate the OpenRCX decks needed by OpenROAD to do parasitic
    extraction.
    '''

    flowname = 'generate_rcx'
    flow = siliconcompiler.Flow(chip, flowname)

    if not extraction_task:
        chip.logger.warn('Valid extraction not specified, defaulting to builtin/nop')
        extraction_task = nop

    flow.node(flowname, 'bench', rcx_bench)
    prev = 'bench'
    for corner in range(corners):
        # For each corner generate a pex step to build the reference SPEF file
        # and the extract step to use the SPEF file to build the new OpenRCX deck
        flow.node(flowname, 'pex', extraction_task, index=corner)
        flow.node(flowname, 'extract', rcx_extract, index=corner)

        if corner == 0:
            prev = 'bench'
            prev_index = 0
        else:
            prev = 'pex'
            prev_index = corner - 1
        # For license restrictions make each pex step dependent on the previous pex step
        flow.edge(flowname, prev, 'pex', head_index=corner, tail_index=prev_index)
        flow.edge(flowname, 'pex', 'extract', head_index=corner, tail_index=corner)
        flow.edge(flowname, 'bench', 'extract', head_index=corner, tail_index=0)
        if corner > 0:
            flow.edge(flowname, 'bench', 'pex', head_index=corner, tail_index=0)

    flow.node(flowname, 'bench', rcx_bench)

    return flow


##################################################
if __name__ == "__main__":
    flow = make_docs(siliconcompiler.Chip('<flow>'))
    flow.write_flowgraph(f'{flow.design}.png', flow=flow.design)
