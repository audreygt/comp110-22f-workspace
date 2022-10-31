"""This specially named module makes the package runnable."""

from exercises.ex09 import constants
from exercises.ex09.model import Model
from exercises.ex09.view_controller import ViewController


def main() -> None:
    """Entrypoint of simulation."""
    model: Model = Model(constants.CELL_COUNT, constants.CELL_SPEED)
    view_controller: ViewController = ViewController(model)
    # coding to continuously update
    view_controller.start_simulation()
    # keeping track of location, state, speed, and count of cells 


if __name__ == "__main__":
    main()