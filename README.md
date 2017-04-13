# Vector_Similarity
* Python, Java implementation of TS-SS called from "A Hybrid Geometric Approach for Measuring Similarity Level Among Documents and Document Clustering"
* I recommend TS-SS instead of Cosine distance or Euclidean distance.

# The reasons are... :

## Cosine drawbacks
![coise_drawback](./image/cosine_drawback.JPG)

## Euclidean drawbacks
![euclidean drawback](./image/euclidean_drawback.JPG)

## Triangle's Area Similarity (TS)
![TS](./image/TS.JPG)

## Sector's Area Similarity (SS)
![SS](./image/SS.JPG)

## TS-SS
![TS_SS](./image/TS_SS.JPG)

## Results
![results](./image/Result.JPG)

## Conclusion
* In biggest dataset, TS-SS outperforms Cosine with a significant difference, while in other datasets TS-SS outperforms Cosine slightly

* Therefore, the significant better result of TS-SS in biggest dataset justifies the robustness and reliability of the model for big data and real world data where the variety of documents/texts are high

## Reference
[1] A Hybrid Geometric Approach for Measuring Similarity Level Among Documents and Document Clustering [link1](https://www.computer.org/csdl/proceedings/bigdataservice/2016/2251/00/2251a142.pdf) [link2](http://ieeexplore.ieee.org/document/7474366/)

