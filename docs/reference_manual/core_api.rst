Core API
----------

This chapter describes all public methods in the SiliconCompiler core Python API. Refer to the User Guide for architecture concepts and the :ref:`glossary` for terminology and keyword definitions.

.. currentmodule:: siliconcompiler

**Schema access:**

.. autosummary::
    :nosignatures:

    ~siliconcompiler.Chip.set
    ~siliconcompiler.Chip.add
    ~siliconcompiler.Chip.get
    ~siliconcompiler.Chip.getkeys
    ~siliconcompiler.Chip.getdict
    ~siliconcompiler.Chip.valid
    ~siliconcompiler.Chip.help
    ~siliconcompiler.Chip.use

**Flowgraph execution:**

.. autosummary::
    :nosignatures:

    ~siliconcompiler.Chip.run
    ~siliconcompiler.Chip.node
    ~siliconcompiler.Chip.edge

**Utility functions:**

.. autosummary::
    :nosignatures:

    ~siliconcompiler.Chip.archive
    ~siliconcompiler.Chip.audit_manifest
    ~siliconcompiler.Chip.calc_area
    ~siliconcompiler.Chip.calc_yield
    ~siliconcompiler.Chip.calc_dpw
    ~siliconcompiler.Chip.check_checklist
    ~siliconcompiler.Chip.check_manifest
    ~siliconcompiler.Chip.check_logfile
    ~siliconcompiler.Chip.clock
    ~siliconcompiler.Chip.create_cmdline
    ~siliconcompiler.Chip.find_files
    ~siliconcompiler.Chip.find_result
    ~siliconcompiler.Chip.grep
    ~siliconcompiler.Chip.hash_files
    ~siliconcompiler.Chip.nodes_to_execute
    ~siliconcompiler.Chip.load_target
    ~siliconcompiler.Chip.read_manifest
    ~siliconcompiler.Chip.show
    ~siliconcompiler.Chip.summary
    ~siliconcompiler.Chip.use
    ~siliconcompiler.Chip.write_manifest
    ~siliconcompiler.Chip.write_flowgraph

.. automodule:: siliconcompiler
    :members:

.. automodule:: siliconcompiler.use
    :members:
