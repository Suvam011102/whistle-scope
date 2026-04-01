from scipy.stats import ttest_1samp

def compute_home_bias(df, min_matches):
    bias_df = (
        df.groupby(["Referee", "HomeTeam"])
          .agg(
              HF=("HF", "mean"),
              AF=("AF", "mean"),
              matches=("HF", "count")
          )
          .query("matches >= @min_matches")
          .reset_index()
    )

    bias_df["HomeBias"] = bias_df["AF"] - bias_df["HF"]

    mean_bias = bias_df["HomeBias"].mean()
    _, p_value = ttest_1samp(bias_df["HomeBias"], 0)

    return {
        "data": bias_df,
        "mean_bias": mean_bias,
        "p_value": p_value
    }
