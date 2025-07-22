# R code for state income histogram
x = state.x77[ , 2]                   # 50 average state incomes in 1977
hist(x, breaks = 8, xlab="Income", main="Histogram of State Income in 1977") 