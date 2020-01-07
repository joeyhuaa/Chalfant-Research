data = read.csv('cde-output2017-18.csv')

## NOTE FOR SAT BENCHMARKS: 
## READING/WRITING: 480
## MATH: 530

# convert all data to integer/numeric
data$num_12e = as.integer(gsub(',','',data$num_12e))
data$num_test = as.integer(gsub(',','',data$num_test))
data$num_ela_curr = as.integer(gsub(',','',data$num_ela_curr))
data$num_ela_prev = as.integer(gsub(',','',data$num_ela_prev))
data$num_ela_total = as.integer(gsub(',','',data$num_ela_total))
data$p_ela = as.numeric(gsub('%','',data$p_ela))
data$num_math_curr = as.numeric(gsub(',','',data$num_math_curr))
data$num_math_prev = as.integer(gsub(',','',data$num_math_prev))
data$num_math_total = as.integer(gsub(',','',data$num_math_total))
data$p_math = as.numeric(gsub('%','',data$p_math))

# delete Sierra County row because no test data was collected
data = data[-c(45),]

# basic overall statistics (nearest integer)
median(data[1:56,2])  # median of med_hh_inc = 57485
mean(data[1:56,2])   # mean of med_hh_inc = 61917
sd(data[1:56,2])   # sd of med_hh_inc = 17671

median(data$num_12e) # median of num_12e = 2408
mean(data$num_12e)  # mean of num_12e = 17165
sd(data$num_12e)   # sd of num_12e = 66045

median(data$num_test) # median of num_test = 921
mean(data$num_test)  # mean of num_test = 8298
sd(data$num_test)   # sd of num_test = 32289

median(data$num_ela_curr)  # mean of num_ela_curr = 831
mean(data$num_ela_curr)   # mean of num_ela_curr = 5879
sd(data$num_ela_curr)   # sd of num_ela_curr = 22723

median(data$num_ela_prev)   # median of num_ela_prev = 0
mean(data$num_ela_prev)    # mean of num_ela_prev = 16
sd(data$num_ela_prev)   # sd of num_ela_prev = 61

median(data$num_ela_total)  # median of num_ela_total = 834
mean(data$num_ela_total)   # mean of num_ela_total = 5895
sd(data$num_ela_total)   # sd of num_ela_total = 22783

median(data$p_ela)   # median of p_ela = 76.7
mean(data$p_ela)  # mean of p_ela = 76
sd(data$p_ela)  # sd of p_ela 10

median(data$num_math_curr)  # median of num_math_curr 527
mean(data$num_math_curr)  # mean = 4190
sd(data$num_math_curr)  # sd = 16144

median(data$num_math_prev) # median of num_math_prev = 0
mean(data$num_math_prev) # mean = 15
sd(data$num_math_prev) # sd = 58

median(data$num_math_total) # median of num_math_total = 527
mean(data$num_math_total) # mean = 4205
sd(data$num_math_total) # sd = 16201

median(data$p_math) # median of p_math = 58
mean(data$p_math) # mean = 55
sd(data$p_math) # sd = 13


# histograms of all columns (except county)
hist(data$med_hh_inc)  # skewed right - curve weighted left, which is expected for income
hist(data$num_12e)  # this dataset is soo skewed bc of huge size inequality b/w counties
hist(data$num_test) # hella skewed left

hist(data$num_ela_curr) 
hist(data$num_math_prev)
hist(data$num_ela_total)
hist(data$p_ela)  # close to gaussian; range 50% - 90%

hist(data$num_math_curr)
hist(data$num_math_prev)
hist(data$num_math_total)
hist(data$p_math) # also close to gaussian; range 30% - 80%

# visuals
scatter.smooth(data$med_hh_inc, data$p_ela)
scatter.smooth(data$med_hh_inc, data$p_math)

library(ggplot2)
ggplot(data, aes(x = med_hh_inc, fill = factor(p_ela))) +
  geom_bar(width = 0.5) +
  xlab('Median Household Income') +
  ylab('% Passed ELA Benchmark') +
  labs(fill = '% Passed')