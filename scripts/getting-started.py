import marimo

__generated_with = "0.19.7"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return


@app.cell
def _():
    import math
    math.sin(3)
    return (math,)


@app.cell
def _(math):
    # Calculate the sin of pi
    math.sin(math.pi)
    return


if __name__ == "__main__":
    app.run()
