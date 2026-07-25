# Probability that the taxi is Blue
P_Blue = 0.15

# Probability that the taxi is Green
P_Green = 0.85

# Probability that the witness correctly identifies Blue
P_SaysBlue_Blue = 0.80

# Probability that the witness says Blue when the taxi is actually Green
P_SaysBlue_Green = 0.20   # (1 - 0.80)

# Bayes' Theorem
P_Blue_SaysBlue = (P_SaysBlue_Blue * P_Blue) / (
    (P_SaysBlue_Blue * P_Blue) +
    (P_SaysBlue_Green * P_Green)
)

# Display the result
print("Probability that the taxi was actually Blue:",
      round(P_Blue_SaysBlue * 100, 2), "%")
