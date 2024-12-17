#ground shipping
ground_weight = 8.4
ground_weight_price = 0
ground_flat_rate = 20

if ground_weight <= 2:
  ground_weight_price = 1.50
  print(f"\nThe cost to ship your {ground_weight:.2f} lb package using Standard Ground Shipping is £{(ground_weight*ground_weight_price)+ground_flat_rate:.2f}")
elif ground_weight >2 and ground_weight <= 6:
  ground_weight_price = 3
  print(f"\nThe cost to ship your {ground_weight:.2f} lb package using Standard Ground Shipping is £{(ground_weight*ground_weight_price)+ground_flat_rate:.2f}")
elif ground_weight > 6 and ground_weight <= 10:
  ground_weight_price = 4
  print(f"\nThe cost to ship your {ground_weight:.2f} lb package using Standard Ground Shipping is £{(ground_weight*ground_weight_price)+ground_flat_rate:.2f}")
else:
  ground_weight_price = 4.75
  print(f"\nThe cost to ship your {ground_weight:.2f} lb package using Standard Ground Shipping is £{(ground_weight*ground_weight_price)+ground_flat_rate:.2f}")

ground_premium_shipping = 125

print(f"\nGround Premium Shipping = £{ground_premium_shipping:.2f}")

#drone shipping

drone_weight = 1.5
drone_weight_price = 0

if drone_weight <= 2:
  drone_weight_price = 4.5
  print(f"\nThe cost to ship your {drone_weight:.2f} lb package using Drone Shipping is £{drone_weight*drone_weight_price:.2f}")
elif drone_weight >2 and drone_weight <= 6:
  drone_weight_price = 9
  print(f"\nThe cost to ship your {drone_weight:.2f} lb package using Drone Shipping is £{drone_weight*drone_weight_price:.2f}")
elif drone_weight > 6 and drone_weight <= 10:
  drone_weight_price = 12
  print(f"\nThe cost to ship your {drone_weight:.2f} lb package using Drone Shipping is £{drone_weight*drone_weight_price:.2f}")
else:
  drone_weight_price = 14.25
  print(f"\nThe cost to ship your {drone_weight:.2f} lb package using Drone Shipping is £{drone_weight*drone_weight_price:.2f}")

print("")