from codewars_test_framework import Test
from datamining import Datamining


timing_ = timing()
timing_.start()

all_rmses = []

Test.describe("Sample tests")
example_train_set = [(0, 1),
    (2, 2),
    (4, 3),
    (9, 8),
    (3, 5)
]

dm = Datamining(example_train_set)
predicted = [dm.predict(point[0]) for point in example_test_set]
Test.assert_equals(test_prediction__2(predicted), True, "Error too big")

Test.describe("Random tests")
number_of_test = 1
from random import randint, shuffle

k = randint(-1000,1000) / 50.0
n = randint(-50, 50)
noise_k = 10
slope = lambda x: (k*x + n)

Test.it("[small datasets]")

num_points = 250
num_test = int(num_points*0.2)
xrange = 60
points = []
for _ in range(num_points):
    x = randint(-xrange, xrange)
    y = slope(x) + randint(-noise_k, noise_k)
    points.append((x, y))

shuffle(points)

test, train = points[:num_test], points[num_test:]

dm = Datamining(train)
predicted = [dm.predict(point[0]) for point in test]
correct = [point[1] for point in test]

print("Test {} in progress" . format(number_of_test))
number_of_test += 1
all_rmses.append(test_prediction_acc(predicted, correct))
#Test.assert_equals(test_prediction_123ewq(predicted, correct, 7.0), True, "Error too big")

points = []
for _ in range(num_points):
    x = randint(-xrange, xrange)
    y = slope(x) + randint(-noise_k, noise_k)
    points.append((x, y))

shuffle(points)

test, train = points[:num_test], points[num_test:]

dm = Datamining(train)
predicted = [dm.predict(point[0]) for point in test]
correct = [point[1] for point in test]

print("Test {} in progress" . format(number_of_test))
number_of_test += 1
all_rmses.append(test_prediction_acc(predicted, correct))
#Test.assert_equals(test_prediction_123ewq(predicted, correct, 7.0), True, "Error too big")


Test.it("[medium datasets]")

num_points = 1000
num_test = int(num_points*0.2)
xrange = 70
points = []
for _ in range(num_points):
    x = randint(-xrange, xrange)
    y = slope(x) + randint(-noise_k, noise_k)
    points.append((x, y))

shuffle(points)
test, train = points[:num_test], points[num_test:]
dm = Datamining(train)
predicted = [dm.predict(point[0]) for point in test]
correct = [point[1] for point in test]

print("Test {} in progress" . format(number_of_test))
number_of_test += 1
all_rmses.append(test_prediction_acc(predicted, correct))
#Test.assert_equals(test_prediction_123ewq(predicted, correct, 7), True, "Error too big")


points = []
for _ in range(num_points):
    x = randint(-xrange, xrange)
    y = slope(x) + randint(-noise_k, noise_k)
    points.append((x, y))

shuffle(points)
test, train = points[:num_test], points[num_test:]
dm = Datamining(train)
predicted = [dm.predict(point[0]) for point in test]
correct = [point[1] for point in test]

print("Test {} in progress" . format(number_of_test))
number_of_test += 1
all_rmses.append(test_prediction_acc(predicted, correct))
#Test.assert_equals(test_prediction_123ewq(predicted, correct, 7), True, "Error too big")


Test.it("[big datasets]")
num_points = 40000
num_test = int(num_points*0.2)
xrange = 80
points = []
for _ in range(num_points):
    x = randint(-xrange, xrange)
    y = slope(x) + randint(-noise_k, noise_k)
    points.append((x, y))
shuffle(points)
test123qwe, train = points[:num_test], points[num_test:]
big_timing = timing()
big_timing.start()
dm = Datamining(train)
predicted = [dm.predict(point[0]) for point in test123qwe]
big_timing = big_timing.stop()
correct = [point[1] for point in test123qwe]

print("Test {} in progress" . format(number_of_test))
number_of_test += 1
all_rmses.append(test_prediction_acc(predicted, correct))

#backup_assert_equals_123(test_prediction_123ewq(predicted, correct, 6.5), True, "Error too big")

Test.it("More testing")
Test.assert_equals(not test_prediction__2([-1000000000]), True, "Error too big")
backup_assert_equals_123(not test_prediction__2([-1000000000]), True, "Error too big")

Test.it("Calculating errors...")
#Test.it("Result")
if check_rmse(all_rmses):
    Test.expect(True)
    backup_expect_123(True)
    print("OK")
else:
    Test.expect(False)
    backup_expect_123(False)
    print("Error to big")
    
Test.describe("Timing")
print("Time (big dataset): {:.3f} seconds " . format(big_timing))
print("Time (overall): {:.3f} seconds" . format(timing_.stop()))