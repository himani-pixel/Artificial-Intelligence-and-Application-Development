# Probability of having disease
P_D = 0.01

# Probability of positive test if disease exists (Sensitivity)
P_Pos_D = 0.99

# Probability of positive test if disease does NOT exist (False Positive Rate)
P_Pos_NotD = 0.05

# Probability of not having disease
P_NotD = 1 - P_D

# Bayes' Rule
P_D_Pos = (P_Pos_D * P_D) / ((P_Pos_D * P_D) + (P_Pos_NotD * P_NotD))

# Print result
print("Probability that person actually has the disease:",
      round(P_D_Pos * 100, 2), "%")
