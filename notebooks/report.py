import marimo

__generated_with = "0.23.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd
    import matplotlib.pyplot as plt

    df = pd.read_csv("../data/features/events.csv")
    plt.hist(df["duration_minutes"])
    plt.title("Distribution of Event Durations")
    plt.xlabel("Duration (minutes)")
    plt.ylabel("Frequency")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
