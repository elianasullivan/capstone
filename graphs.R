#this is written in R

#####THIS IS FOR THE ACE SCORE GRAPH#############

library(ggplot2)
library(scales)

data <- read.csv("/Users/elianasullivan/Documents/Minerva/last one/second semester/capstone/full clean data.csv")

ace_score <- (data$ACEDEPRS+data$ACEDIVRC+data$ACEDRINK+data$ACEDRUGS+data$ACEHURT+data$ACEHVSEX+data$ACEPRISN+data$ACESWEAR+data$ACETOUCH+data$ACETTHEM+data$ACEPUNCH)
ace_score[ace_score > 4] <- 4
ace_data <- cbind(data,ace_score)


# Barplot of ACE prevalence
freqs <- c()
for (i in 0:4) {
  {freqs <- c(freqs,(sum(ace_data$ace_score == i)))
  }}
freqs

bar <- data.frame(
  group = ((freqs)),
  value = c("0","1","2","3","4+"),
  ace_labels= (percent(freqs/nrow(ace_data)))
)

bar$value <- factor(bar$value, levels = bar$value[c(0:5)])
bp<- ggplot(bar, aes(x=value, y=group, label = ace_labels))+
  geom_bar(stat="identity",color = "black", fill = "steelblue")+geom_text(size=5, position=position_stack(vjust=0.5), color = "white")
bp + ggtitle("ACE Score Distribution in BRFSS 2010 Survey (N = 16,039)") +
  xlab("Number of ACEs") + ylab("Number of Responses")+
  theme(plot.title = element_text(size=22),
        axis.text=element_text(size=16),
        axis.title.x=element_text(size=16),
        axis.title.y=element_text(size=16))


###################### PREVALENCE OF ACES ####################################
#prevalence of each ACE
install.packages("stringr")
library(stringr)
install.packages("scales")
library(scales)
library(ggplot2)

ace_names = c("Depressed or mentally ill parent","Alcoholic parent", "Drug abuse (by parent)","Incarcerated parent","Divorced parents", "Parents violent towards one another", "Physical abuse","Verbal abuse","Sexual Abuse")

#collects proportions of each outcome
props <- c()
for (x in data[, 3:10]){
  props <- c(props, (sum(x))/16039)
}

# calculates the prevalence of sexual abuse
# because it is split across 3 categories in BRFSS
s_value <- 0
start <- data$ACEHVSEX+data$ACETOUCH+data$ACETTHEM
for (x in start){
  if (x != 0) {
    s_value <- s_value + 1
  }
}
s_abuse <- (s_value/16039)
props <- c(props, s_abuse)

#make a data frame with the proportions, names, and labels
ace_prev <- data.frame("value" = ace_names, "group" = props, "ace_labels" = percent(props))

bp<- ggplot(ace_prev, aes(x=value, y=group, label = ace_labels))+ coord_flip() +
  geom_bar(stat="identity",color = "black", fill = "#089B9B")+geom_text(size=5, position=position_stack(vjust=0.5), color = "white")
bp + ggtitle("Prevalence of Adverse Childhood Experiences (N = 16,039)") +
  xlab("Adverse Childhood Experiences (ACEs)") + ylab("Proportion of Respondents with Experience")+
  theme(plot.title = element_text(size=24),
        axis.text=element_text(size=16),
        axis.title.x=element_text(size=16),
        axis.title.y=element_text(size=16))


###################################THIS IS FOR THE STACKED BAR CHART FOR THE HEALTH OUTCOME TOOL#######################
install.packages("tidyverse")
library(tidyverse)

#this is for making the stacked visualization
viz <- data.frame(Type = c("no", "yes_w_aces", "yes"), 
                  Proportion = c(30, 13, 57))
viz <- viz %>% 
  mutate(ace = "Probability of Anxitety")

viz$Type <- factor(viz$Type, levels = viz$Type[c(0:3)])

ggplot(viz, aes(x = ace, y = Proportion, fill = Type)) +
  geom_col() +
  coord_flip() +
  #could prob just put in percent(number) instead of proportion + % and hopefully would work
  geom_text(aes(label = paste0(Proportion, "%")),
            position = position_stack(vjust = 0.5)) +
  scale_fill_brewer(palette = "Set2") +
  theme_minimal(base_size = 14) +
  ylab("Percentage") +
  xlab(NULL)
#############################