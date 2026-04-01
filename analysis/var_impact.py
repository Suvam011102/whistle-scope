def compute_var_impact(df):
    df = df.copy()
    df["CardsPerFoul"] = df["TotalCards"] / df["TotalFouls"]

    summary = (
        df.groupby("VAR_Era")
          .agg(
              avg_fouls=("TotalFouls", "mean"),
              avg_cards=("TotalCards", "mean"),
              avg_cards_per_foul=("CardsPerFoul", "mean")
          )
          .reset_index()
    )

    return summary, df
