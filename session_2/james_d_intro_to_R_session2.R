# James_d introduction to R, session 2;
# here we'll be cleaning/analyzing some of James' own data;
# data is downloaded from qualtrics
#
# things he would like to work on:

# Changing qualitative responses into numeric ones 
# Deleting rows/columns 
# Conducting t-tests 
# Conducting ANOVAs 
library(dplyr)


## loading data:

# first set up our working directory:

workingDirectory = "~/Desktop/tutoring/session_2"

setwd(workingDirectory)

# what files do we have in our directory?

list.files()

df = read.csv("Value2.csv", header = TRUE) # load in qualtrics data

head(df)

View(df)

summary(df)

glimpse(df)

## deleting rows and colums from a dataframe


# deleting rows:



# looks like there are a few unnecessary rows on the top; let's clean them up:

# first two rows appear to be superfluous:

# remove manually (base R)):

iris = iris

iris_head = head(iris)

iris_head[2,2]

blah = df[-c(1,2), ]# drop first two rows

# remove manually (dplyr)):

blah2 = slice(df,7:148)

# see also filter()

df_filtered = filter(df, Consent == 'Yes') # NB: this includes a preview

# do this in a smarter way:

unique(df$Status)

df_filtered = filter(df, Status == 'IP Address')

obs = df$Duration..in.seconds.

as.numeric(as.character(obs))

df_slow_resp = filter(df, Duration..in.seconds. > 4)





# remove survey preview rows?


# deleting columns:

iris = iris

colnames(df)

cols_to_exclude = c("Species","Petal.Width")

iris_subset = select(iris, -Species) # one column

# multiple columns (see help; NB the minus sign)

?select

iris_subset2 = select(iris, -one_of(cols_to_exclude))

# select by number:

select(iris, 1:2, 4)

# select with a match:

select(iris, contains("Pet"))

# ends with:

select(iris, ends_with("h"))





# df cols to remove:

unique(df$RecipientLastName)
unique(df$RecipientFirstName)

# both look empty; let's get rid of them:

cols_to_exclude = c('RecipientLastName','RecipientFirstName')

blah3 = select(blah2, -one_of(cols_to_exclude))


# do it in order, with piping:
# NB: the advantage here is that we don't need to keep 
# messy intermediate variables, we get to write data manipulation
# processes in the order we want them; output of a dply function is 
# a dataframe, input is a dataframe

test_df = df %>%
  slice(3:148) %>% # remove first two rows
  select(-one_of(cols_to_exclude)) # remove specific columns



## changing qualitative responses into numeric ones:

# which values do we want to change?



# summary statitics:

iris.means = iris %>%
  group_by(Species) %>%
  summarise(
    mean_sepal_length = mean(Sepal.Length),
    mean_sepal_width = mean(Sepal.Width),
    mean_petal_length = mean(Petal.Length),
    mean_petal_width = mean(Petal.Width),
    sum_sepal_length = sum(Sepal.Length)
  )

View(iris.means)





x <- mtcars[1:3]
y <- mtcars[4:6]
cor(x, y)


# good resource for ezanova in R: https://www.r-statistics.com/tag/ezanova/







