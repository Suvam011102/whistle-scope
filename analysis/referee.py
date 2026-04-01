def compute_referee_stats(df, min_matches):
    return (
        df.groupby("Referee")
          .agg(
              matches=("Referee", "count"),
              avg_fouls=("TotalFouls", "mean"),
              avg_cards=("TotalCards", "mean")
          )
          .query("matches >= @min_matches")
          .reset_index()
    )
