from datetime import datetime
import click
from model.execution import execute_experiment



@click.command()
def main() -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    df = execute_experiment()
    df.to_pickle(
            f"data/simulations/single-run-{timestamp}.pkl.gz", compression="gzip")

if __name__ == "__main__":
    main()