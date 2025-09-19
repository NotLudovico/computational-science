import marimo

__generated_with = "0.16.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt
    plt.style.use("default")
    return mo, np, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Polynomial Regression""")
    return


@app.cell
def _(mo):
    sigma = mo.ui.number(value=1, label=r"$\sigma$")
    N = mo.ui.number(value=100, label="Number")
    degree = mo.ui.number(value=1, step=1, label="Degree")
    test_pct = mo.ui.slider(start=0, value=20, stop=100, label="% test")

    N, sigma, degree, test_pct
    return N, degree, sigma


@app.cell
def _(N, degree, mo, np, plt, sigma):
    # --- Real function: swap as needed, e.g. return np.sin(x) ---
    def f(x):
        return np.sin(x)

    # --- Settings ---
    np.random.seed(42)
    x_min, x_max = 0.0, 10.0

    # --- Generate data (real + noisy) ---
    x = np.linspace(x_min, x_max, N.value)
    y_real_samples = f(x)
    y_noisy = y_real_samples + np.random.normal(0.0, sigma.value, size=N.value)


    # --- Smooth grid for plotting curves ---
    xplot = np.linspace(x_min, x_max, 1000)
    y_real = f(xplot)

    aaa = np.polyfit(x, y_noisy, deg=degree.value)
    print(aaa)
    bbb = np.polyval(aaa, xplot)

    plt.plot(xplot, y_real, label="Real function")
    plt.plot(xplot, bbb)
    plt.scatter(x, y_noisy, s=20, alpha=0.8, label="Noisy samples")
    plt.xlabel("x"); plt.ylabel("y")
    plt.title(f"$\sigma$ = {sigma.value}, polyfit with degree = {degree.value}")
    plt.ylim(-5,5)
    plt.legend()
    mo.center(plt.gca())
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
