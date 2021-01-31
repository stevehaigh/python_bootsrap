import click


@click.command()
@click.option("--my_arg", help="A command line argument")
def main(my_arg :str) -> None:
    """Sample main method. Add implementation here!

    Args:
        my_arg (str):Sample argument, replace this!
    """
    print(my_arg)
    return my_arg


if __name__ == "__main__":
    main()