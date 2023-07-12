from rpy2.robjects.packages import importr
from rpy2 import robjects

# base = importr('base')
utils = importr('utils')
utils.chooseCRANmirror(ind=1)
utils.install_packages('baseballr')
robjects.r('library(baseballr)')
robjects.r('library(dplyr)')
data = robjects.r('bref_daily_batter("2020-08-01", "2020-10-03")')
print(data)
