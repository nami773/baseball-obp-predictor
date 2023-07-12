from rpy2.robjects.packages import importr
from rpy2.robjects.conversion import localconverter
from rpy2 import robjects
import rpy2.robjects as ro
from rpy2.robjects import pandas2ri
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import make_pipeline
from sklearn.tree import DecisionTreeRegressor
from sklearn import tree
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score


utils = importr('utils')
utils.chooseCRANmirror(ind=1)
utils.install_packages('baseballr')
robjects.r('library(baseballr)')
robjects.r('library(dplyr)')
data = robjects.r('bref_daily_batter("2020-08-01", "2020-10-03")')
with localconverter(ro.default_converter + pandas2ri.converter):
  df = ro.conversion.rpy2py(data)

df.drop(['bbref_id', 'Name', 'season', 'PA', 'X1B', 'X2B', 'X3B', 'BB', 'IBB',
        'uBB', 'HBP', 'SH', 'SF', 'GDP', 'CS', 'SLG', 'OPS'],  axis=1)

# If OBP is null, drop all the null rows
df = df[df['OBP'].notna()]

print(df)

y = df["OBP"]
x = df.drop("OBP", axis=1)

num_attribs = ["Age", "G", "AB", "R", "H", "HR", "RBI", "SO", "SB", "BA"]
cat_attribs = ["Level", "Team"]

num_pipeline = make_pipeline(
    SimpleImputer(strategy="median")
)

cat_pipeline = make_pipeline(
    SimpleImputer(strategy="constant", fill_value="Unknown"),
    OneHotEncoder(handle_unknown="ignore")
)

preprocessing = ColumnTransformer([
    ("cat", cat_pipeline, cat_attribs),
    ("num", num_pipeline, num_attribs)])

x = preprocessing.fit_transform(x)

reg = DecisionTreeRegressor(random_state=42, max_depth=4)
reg.fit(x, y)

# The image must be large in order to fully see all the nodes
plt.figure(figsize=(20, 20))
tree.plot_tree(reg, fontsize=6)
plt.show()

tree_rmse = -cross_val_score(reg, x, y, scoring="neg_mean_squared_error", cv=10)
print(f"Average RSME score is {sum(tree_rmse)/len(tree_rmse)}")
