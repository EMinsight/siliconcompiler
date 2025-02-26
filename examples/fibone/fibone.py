import siliconcompiler
import os


def main():
    root = os.path.dirname(__file__)
    chip = siliconcompiler.Chip('mkFibOne')
    chip.input(f'{root}/FibOne.bsv')
    chip.set('option', 'frontend', 'bluespec')
    # default Bluespec clock pin is 'CLK'
    chip.clock(pin='CLK', period=5)
    chip.load_target("freepdk45_demo")
    chip.run()
    chip.summary()
    chip.show()


if __name__ == '__main__':
    main()
