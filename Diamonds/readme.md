# Diamonds

I came across this dataset a while back while looking through I think the MBA website for either the Univerity of Virginia or Harvard website. It was titled "Sarah Gets a Diamond" and immediately two things came to mind. The first was that it would be good for a comarison of regression models.

The second is harder for me to pin down. In part it was how very traditional it was. The other part was how odd picking out an engagement ring would be based strictly off the numbers. I understand not everyone is of substantial means or can bank on high earning potential earnings like HBS grads can and so are price sensitive. But I can't imagine anyone just basing it off of either caret per dollar or some other decision making calculus. There's a lot of hopes and emotions tied up in that. And if there's not, that probably very telling. 

Still, it's a good dataset though, in hindsight, I don't think this is the same data set and certainly not the one marked on HBS's site as that one has a paltry 6000 diamonds whereas this has just under 220,000 diamonds.

<br>

# Notes
 1. Because it was getting way too long for a single notebook, this project has been broken into three different notebooks: Data Wrangling, EDA, and Models.
 2. Data for EDA and Models comes from a pickle file generated in the Data Wrangling notebook. Pickle files aren't secure. They allow unvalidated and potentially malicious code to run. So, for those who approach life with a "F**k it, YOLO!" attitude, I commend your confidence. For the paranoid who think there is a malicious actor at every turn, I respect your security awareness. Simply step through the code in the Data Wrangling notebook to assure yourself that the pickle file is free from any ill intent. You'll only need to do this once.

<br>

# Current situation:

## EDA
### What I would call the first pass is done. Key takeaways so far:
 * 73% of diamonds are round cut
 * Oval, Pear, and Emerald are the next most popular, ranging between 3%-6% each
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
  * Decision Trees are marginally better than LR. Fast but max out at depth of 3. Overall, Decision Trees has a 13.3% improvement over baseline in RMSE and a 10.9% improvement over the baseline R2.

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
