# Diamonds

I came across this dataset a while back while looking through the Harvard Business School's website. It was titled "Sarah Gets a Diamond". Two things came to mind. The first was that it would be good for a regression model. The second is harder for me to pin down. Part of it has to do with how odd picking out an engagement ring would be based strictly off the numbers. I get price because not everyone is of substantial means or can bank on high earning potential earnings, like the HBS grads can. The other is how very traditional this all is.

Still, it's a good dataset.

<br>

# Notes
 1. Because it was getting way too long for a single notebook,  this project has been broken into three different notebooks: Data Wrangling, EDA, and Models.
 2. Data for EDA and Models comes from a pickle file generated in the Data Wrangling notebook. Pickle files aren't secure. They allow unvalidated and potentially malicious code to run.   So, for those who approach life with a "F**k it, YOLO!" attitude, I commend your confidence. For the paranoid who think there is a malicious actor at every turn, I commend your caution. Simply delete the file and either run or step through the Data Wrangling notebook and new pickle file will be generated. You'll only need to do this once.


<br>

# Current situation:

## EDA
### What I would call the first pass is done. Key takeaways so far:
 * 73% of diamonds are round cut
 * Oval, Pear, and Emerald are the next most popular, ranging between 6.3%-4.5%
 * jfkdlj

<br>

### Outstanding questions:

 * jfdlkfd
 * jfkdlj


<br>

---

##  Models --
   * Linear Regression as a baseline
  ```
  72.4 ms ± 5.24 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)

  RMSE: 16057.10618458078
  R2  : 0.7728174575988863
  ```

  * RandomForestRegresson is considerably better but takes considerably longer.
  ```
  1min 19s ± 648 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

  RMSE: 9536.786677216744
  R2  : 0.9262440179416279
  ```
  * Decision Trees are marginally better than LR. Fast but max out at depth of 3. Overall, Decision Trees has a 13.3 % improvement over baseline in RMSE and a 10.9 % improvement in R2.

  ```
  Not timed but about at fast as LR 
  RMSE: 13921.257325084407
  R2  : 0.8350244922620658
  ```
  * Extreme Gradient Boosting (aka, xgboost)
  ```
  RMSE: 9098.612575706364
  R2  : 0.9331040969124664
  ```
  Good performance and so much faster than Random Forrest Regression. And this is for an untuned model. Now let's see about tuning it.