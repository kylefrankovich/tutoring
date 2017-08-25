# James_d introduction to R;
# here we cover loading data into dataframes, selecting/manipulating data
# from dataframes, installing packages, summary statistics, simple data viz,
# stats/linear model

## loading data:

# first set up our working directory:

workingDirectory = "~/Desktop/tutoring"

setwd(workingDirectory)

# here we load data that's built into R:

iris_df = iris

blah = c(1,2,3,4)

View(iris_df)

# data(package="datasets") # view all pre-installed datasets

# export dataframe to .csv:

write.csv(iris_df, file = "iris_data.csv", row.names = FALSE); # row.names argument excludes row numbering

getwd() # gets current working directory

list.files() # show contents of directory

?write.csv # help for the function we're calling

# load back in our .csv data:

df = read.csv("iris_data.csv") # load in iris data

# peek at data:

View(df)

head(df)

tail(df)

summary(df)

## manipulation of data:

blah = 'Species'

df[blah] # view a column

df[1] # view a column by column number

# or

df$Species

df$Sepal.Width


df[2,] # view a row

# what unique species do we have?

uniqueSpecies = unique(df$Species)

uniqueSepalWidth = unique(df$Sepal.Width)

uniquePetalLength = unique(df$Petal.Length)

length(uniquePetalLength)

?unique

# how many unique species?

length(unique(df$Species))

length(uniqueSepalWidth)

# installing packages, introduction to tidyverse:

install.packages("dplyr")

library(dplyr)

?dplyr

# subsetting data with dplyr:

# select specific rows:

dplyr::filter(df,Sepal.Width >= 3) # extract rows via logical statement

df_setosa = dplyr::filter(df,Species == "setosa") # only setosa

df_versicolor_virginica = dplyr::filter(df,Species != 'setosa') # the other two species


df_select_cols = dplyr::select(df,Sepal.Length, Petal.Length, Species)

create_vec = c(1,2,3,4)


head(df_select_cols)

# rename column example (note we only change 2 of the 3):
df_select_cols = rename(df_select_cols, 
                        sepal_length = Sepal.Length,
                        petal_length = Petal.Length)

head(df_select_cols)


# summary statitics:

df.means = df %>%
  group_by(Species) %>%
  summarise(
    mean_sepal_length = mean(Sepal.Length),
    mean_sepal_width = mean(Sepal.Width),
    mean_petal_length = mean(Petal.Length),
    mean_petal_width = mean(Petal.Width),
    sum_sepal_length = sum(Sepal.Length)
  )


# sanity check:

df_setosa = filter(df, Species == "setosa")

mean_sepal_length_setosa = mean(df_setosa$Sepal.Length) # does this match our piping operation above?

sum(df$Sepal.Length)

sqrt(sum(df$Sepal.Length))

## data visualization:

# let's make a simple bar graph for our summary stats above:

# here we use ggplot:

install.packages('ggplot2')

library(ggplot2)

# scatterplot:

ggplot(data=df, aes(x=Sepal.Length, y=Sepal.Width)) + geom_point()

# or create as variable:
myplot <- ggplot(data=df, aes(x=Sepal.Length, y=Sepal.Width))

myplot + geom_point()


# change size of points:

ggplot(data=df, aes(x=Sepal.Length, y=Sepal.Width)) + geom_point(size=3)

?ggplot

g = ggplot(df.means, aes(factor(Species)))

# lets look at species by color:

ggplot(data=df, aes(x=Sepal.Length, 
                    y=Sepal.Width, 
                    color=Species)) + geom_point(size=3)

# color and shape:

ggplot(data=df, aes(x=Sepal.Length, 
                      y=Sepal.Width, 
                      color=Species, 
                      shape=Species)) + geom_point(size=3)

# add a linear fit:

ggplot(df, aes(x=Sepal.Length, 
                 y=Sepal.Width, 
                 color=Species)) + geom_point() + stat_smooth(method="lm")

# let's export our pretty plot:

plot_path = getwd()
plot_path = '~Users/'

ggsave(file = "pretty_plot.pdf", 
       path = plot_path, 
       width = 8, 
       height = 6)

?ggsave

# bar plot:

ggplot(df, aes(Species, Sepal.Length)) + geom_bar(stat = "identity")

ggplot(df, aes(Species, Petal.Length)) + geom_bar(stat = "identity")


# stats!

# predictiing petal.width:

?lm

model1 <- lm(Petal.Width ~ Sepal.Length
             + Sepal.Width + Petal.Length + Sepal.Length * Sepal.Width,
             data = df)

model1

summary(model1)

