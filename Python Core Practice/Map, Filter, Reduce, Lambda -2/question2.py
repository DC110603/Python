"""3. Given a list:
nums = [12, 15, 7, 18, 20, 21, 25]
Use filter() and lambda to keep numbers that are divisible by 3 OR divisible by
5 but NOT divisible by both.
Explain how the logical condition works."""


nums = [12, 15, 7, 18, 20, 21, 25]
nums2=list(filter(lambda x: 0 if x%3==0 or x%5==0 and (x%3==0 and x%5==0) else x,nums))
print(nums2)