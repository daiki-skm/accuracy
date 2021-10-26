# accuracy
This repository uses the news api to scrape news articles and then calculate their accuracy.  

## What is accuracy?

![スクリーンショット 2021-10-26 12 37 37](https://user-images.githubusercontent.com/69021549/138804873-ba4faf81-8ab4-46a2-b143-1d20f8af4ebb.png)

accuracy = (TP + TN) / (TP + TN + FP + FN)  
precision = TP / (TP + FP)  
recallate = TP / (TP + TN)  

## How to run
```
python3 main.py
```

## Result
```
Size of Positive line document data =  56
Size of Negative line document data =  51
Size of Total line document data =  107
Size of Dictionary =  21176
Number of Train Data =  64
Number of Test Data =  43
Using test data set, Accuracy =  0.9534883720930233
confusion matrix
[[17  2]
 [ 0 24]]
precision 1.0
recallate 0.8947368421052632
```

## Reference
https://aiacademy.jp/media/?p=258  
