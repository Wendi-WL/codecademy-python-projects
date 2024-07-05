weight = 1.5

# Ground Shipping
cost_ground = 20.00
if weight <= 2:
  cost_ground += 1.50 * weight
elif weight <= 6:
  cost_ground += 3.00 * weight
elif weight <= 10:
  cost_ground += 4.00 * weight
else:
  cost_ground += 4.75 * weight
print("Ground Shipping: $" + str(cost_ground))

# Ground Shipping Premium
cost_ground_premium = 125.00
print("Ground Shipping Premium: $", str(cost_ground_premium))

# Drone Shipping
if weight <= 2:
  cost_drone = 4.5 * weight
elif weight <= 6:
  cost_drone = 9.00 * weight
elif weight <= 10:
  cost_drone = 12.00 * weight
else:
  cost_drone = 14.25 * weight

print("Drone Shipping: $", str(cost_drone))