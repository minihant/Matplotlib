# Top 50 matplotlib Visualizations – The Master Plots (with full python code)

> https://www.machinelearningplus.com/plots/top-50-matplotlib-visualizations-the-master-plots-python/#1.-Scatter-plot
> https://github.com/selva86/datasets


## __Correlation(相關性)__
1. Scatter plot
2. Bubble plot with Encircling
3. Scatter plot with line of best fit
4. Jittering with stripplot
5. Counts Plot
6. Marginal Histogram
7. Marginal Boxplot
8. Correlogram
9. Pairwise Plot

## __Deviation(偏差)__
1. Diverging Bars
2. Diverging Texts
3. Diverging Dot Plot
4. Diverging Lollipop Chart with Markers
5. Area Chart

## __Ranking(排行)__
1. Ordered Bar Chart
2. Lollipop Chart
3. Dot Plot
4. Slope Chart
5. Dumbbell Plot

## __Distribution(分佈)__
1. Histogram for Continuous Variable
2. Histogram for Categorical Variable
3. Density Plot
4. Density Curves with Histogram
5. Joy Plot
6. Distributed Dot Plot
7. Box Plot
8. Dot + Box Plot
9. Violin Plot
10. Population Pyramid
11. Categorical Plots

## __Composition(組成)__
1. Waffle Chart
2. Pie Chart
3. Treemap
4. Bar Chart

## __Change(更改)__
1. Time Series Plot
2. Time Series with Peaks and Troughs Annotated
3. Autocorrelation Plot
4. Cross Correlation Plot
5. Time Series Decomposition Plot
6. Multiple Time Series
7. Plotting with different scales using secondary Y axis
8. Time Series with Error Bands
9. Stacked Area Chart
10. Area Chart Unstacked
11. Calendar Heat Map
12. Seasonal Plot

## __Groups(數組)__
1. Dendrogram
2. Cluster Plot
3. Andrews Curve
4. Parallel Coordinates

----

## __A. Correlation__
### 1. Scatter plot
> Scatteplot是用於研究兩個變量之間關係的經典基礎圖。 如果數據中有多個組，則可能需要以不同的顏色可視化每個組。 在matplotlib中，您可以使用plt.scatterplot（）方便地執行此操作。
![Alt text](resource/1_Scatterplot_Matplotlib-min.png){ width: 100px; }
### 2. Bubble plot with Encircling
> 有時您想在邊界內顯示一組點以強調其重要性。 在此示例中，您從應該被環繞的數據框中獲取記錄，並將其傳遞給下面的代碼中描述的encircle（）。
![Alt text](resource/2_Bubble_Plot-min.png){ width: 100px; }
### 3. Scatter plot with linear regression line of best fit
> 如果您想了解兩個變量如何相對變化，則最好的方法就是走。 下圖顯示了數據中各組之間的最佳擬合線之間的差異。 要禁用分組並僅為整個數據集繪製一條最合適的線，請從下面的sns.lmplot（）調用中刪除hue ='cyl'參數。
![Alt text](resource/3_1_Scatterplot_with_linesofbestfit_Seaborn-min.png){ width: 100px; }
### 4. Jittering with stripplot
> 通常，多個數據點具有完全相同的X和Y值。 結果，多個點相互繪製並隱藏。 為避免這種情況，請稍稍抖動點，以便您可以直觀地看到它們。 使用seaborn的stripplot（）這樣做很方便。
![Alt text](resource/4_Jittering_with_Stripplot_Seaborn-min.png){ width: 100px; }
### 5. Counts Plot
> 避免點重疊問題的另一種選擇是增加點的大小，具體取決於該點上有多少點。 因此，點的大小越大，周圍的點的集中度就越大。
![Alt text](resource/5_Counts_plot_Matplotlib-min.png){width:100px;}
### 6. Marginal Histogram
> 邊際直方圖沿X和Y軸變量具有直方圖。 這用於可視化X和Y之間的關係以及X和Y的單變量分佈。 如果經常在探索性數據分析（EDA）中使用此圖。
![Alt text](resource/6_Marginal_histogram_Matplotlib-min.png){width:100px;}
### 7. Marginal Boxplot
> 邊緣框圖的作用與邊緣直方圖相似。但是，箱線圖有助於查明X和Y的中位數，第25和第75個百分位數。
![Alt text](resource/7_Marginal_boxplot_Matplotlib-min.png){width:100px;}
### 8. Correllogram
> 關聯圖用於直觀地查看給定數據幀（或2D數組）中所有可能的數字變量對之間的相關性度量。
![Alt text](resource/8_Correlogram_Matplotlib-min.png){width:100px;}

### 9. Pairwise Plot
> 在理解分析中所有可能的數字變量對之間的關係時，成對繪圖是最喜歡的。 它是用於雙變量分析的必備工具。
![Alt text](resource/9_Pairplot_lines_Seaborn-min.png){width:100px;}
---

## __B. Deviation__
### 10. Diverging Bars
> 如果要查看項目基於單個度量標準的變化方式並可視化此變化的順序和數量，則分散條是一個很好的工具。 它有助於快速區分數據中組的性能，並且非常直觀，可以立即傳達要點。
![Alt text](resource/10_Diverging_bars_Matplotlib-min.png){width:100px;}
### 11. Diverging Texts
> 分隔文本類似於分隔條，如果您希望以一種美觀和可表達的方式顯示圖表中每個項目的值，則首選文本。
![Alt text](resource/11_Diverging_Textbars_Matplotlib-min.png){width:100px;}
### 12. Diverging Dot Plot
> 發散點圖也類似於發散條。 但是，與散佈條相比，條的不存在會降低組之間的對比度和差異。
![Alt text](resource/12_Diverging_DotPlot_Matplotlib-min.png){width:100px;}
### 13. Diverging Lollipop Chart with Markers
> 帶有標記的棒棒糖通過將重點放在您要引起注意的重要數據點上並在圖表中適當地進行推理，提供了一種可視化差異的靈活方式。
![Alt text](resource/13_Diverging_Lollipop_Matplotlib-min.png){width:100px;}
### 14. Area Chart
> 通過為軸和線之間的區域著色，面積圖不僅將重點放在峰谷和谷底，而且還將重點放在高點和低點的持續時間上。 高點持續時間越長，線下面積越大。
![Alt text](resource/14_AreaChart_Matplotlib-min.png){width:100px;}

---
## __C. Ranking__
### 15. Ordered Bar Chart
> 有序條形圖有效地傳達了項目的排名順序。 但是，將指標的值添加到圖表上方，用戶可以從圖表本身獲取準確的信息。
![Alt text](resource/15_Ordered_Barchart_Matplotlib-min.png){width:100px;}

### 16. Lollipop Chart
> 棒棒糖圖表在視覺上令人愉悅，其功能與訂購條形圖相似。
![Alt text](resource/16_Lollipop_Chart_Matplotlib-min.png){width:100px;}

### 17. Dot Plot
> 點狀圖傳達了項目的等級順序。 並且由於它是沿水平軸對齊的，因此您可以更輕鬆地可視化這些點之間的距離。
![Alt text](resource/17_DotPlot_Matplotlib-min.png){width:100px;}

### 18. Slope Chart
> 斜率圖最適合比較給定人員/項目的“之前”和“之後”位置。
![Alt text](resource/18_Slopechart_Matplotlib-min.png){width:100px;}

### 19. Dumbbell Plot
> 啞鈴圖傳達了各個項目的“之前”和“之後”位置以及這些項目的排名順序。 如果您想可視化特定項目/計劃對不同對象的效果，則它非常有用。
![Alt text](resource/19_Dumbbell_Chart_Matplotlib-min.png){width:100px;}
---
## __D. Distribution__
### 20. Histogram for Continuous Variable
> 直方圖顯示給定變量的頻率分佈。 下圖基於分類變量對頻率條進行了分組，從而對連續變量和分類變量串聯在一起有更深入的了解。
![Alt text](resource/20_Histogram_Continuous_Matplotlib-min.png){width:100px;}

### 21. Histogram for Categorical Variable
> 分類變量的直方圖顯示該變量的頻率分佈。 通過對條進行著色，您可以將分佈與代表顏色的另一個分類變量關聯起來。
![Alt text](resource/21_Histogram_Barchart_Matplotlib-min.png){width:100px;}
### 22. Density Plot
> 密度圖是可視化連續變量分佈的常用工具。 通過使用“ response”變量對它們進行分組，您可以檢查X和Y之間的關係。以下情況僅出於代表性的目的，描述城市里程的分佈相對於汽缸數的變化。
![Alt text](resource/22_DensityPlot_Matplotlib-min.png){width:100px;}
### 23. Density Curves with Histogram
> 帶有直方圖的密度曲線將兩個圖所傳達的集體信息匯總在一起，因此您可以將它們都放在一個圖中而不是兩個圖中。
![Alt text](resource/23_DensityPlot_With_Histogram_Matplotlib-min.png){width:100px;}
### 24. Joy Plot
> Joy Plot允許不同組的密度曲線重疊，這是一種可視化大量組相對於彼此分佈的好方法。 它看起來令人賞心悅目，並且清楚地傳達了正確的信息。 可以使用基於matplotlib的joypy軟件包輕鬆構建它。
![Alt text](resource/24_JoyPlot_joypy-min.png){width:100px;}
### 25. Distributed Dot Plot
> 分佈點圖顯示了按組劃分的點的單變量分佈。 點越暗，該區域中數據點的集中度越高。 通過對中位數進行不同的著色，各組的實際位置會立即變得明顯。
![Alt text](resource/25_Distributed_Dotplot_Matplotlib-min.png){width:100px;}
### 26. Box Plot
> 箱形圖是可視化分佈的一種好方法，同時牢記中位數，第25個第75個四分位數和離群值。 但是，在解釋方框的大小時需要小心，這可能會扭曲該組中包含的點數。因此，手動在每個框中提供觀察次數可以幫助克服此缺點。例如，左邊的前兩個框具有相同大小的框，即使它們分別具有5和47個obs。 因此，有必要寫下該組中的觀察數。
![Alt text](resource/26_Boxplots_Matplotlib-min.png){width:100px;}

### 27. Dot + Box Plot
> 點+箱形圖以箱形圖的形式傳達相似的信息。 此外，這些點還使您感覺到每個組中有多少個數據點。
![Alt text](resource/27_Dot_Box_Plot_Seaborn-min.png){width:100px;}

### 28. Violin Plot
> 小提琴圖是箱形圖的視覺替代。 小提琴的形狀或面積取決於其持有的觀察次數。 但是，小提琴圖很難閱讀，在專業環境中不常用。
![Alt text](resource/28_Violin_Plot_Seaborn-min.png){width:100px;}

### 29. Population Pyramid
> 人口金字塔可用於顯示按體積排序的組的分佈。 或者，它也可以用於顯示人口的逐步過濾，因為下面將使用它來顯示有多少人通過營銷渠道的每個階段。
![Alt text](resource/29_PyramidPlot_Matplotlib-min.png){width:100px;}

### 30. Categorical Plots
> seaborn庫提供的分類圖可用於可視化兩個或更多個分類變量彼此之間的計數分佈。
![Alt text](resource/30_CatPlots_1_Seaborn-min.png){width:100px;}
---
## __E. Composition__
### 31. Waffle Chart
> 華夫餅圖可以使用pywaffle程序包創建，並用於顯示較大人群中的組組成。
![Alt text](resource/31_WaffleChart_1_Pywaffle-min.png){width:100px;}

### 32. Pie Chart
> 餅圖是顯示組組成的經典方法。 但是，如今一般不建議使用它，因為餡餅部分的面積有時會誤導人。 因此，如果您要使用餅圖，強烈建議您明確寫下餅圖各部分的百分比或數字。
![Alt text](resource/32_PieChart_1_Matplotlib-min.png){width:100px;}

### 33. Treemap
> 樹形圖類似於餅形圖，並且可以更好地完成工作，而不會誤導每個組的貢獻。
![Alt text](resource/33_Treemap_squarify-min.png){width:100px;}

### 34. Bar Chart
> 條形圖是一種基於計數或任何給定指標可視化項目的經典方法。 在下面的圖表中，我為每個項目使用了不同的顏色， 但是您通常可能希望為所有項目選擇一種顏色，除非您按組對它們進行著色。 顏色名稱存儲在以下代碼中的all_colors中。您可以通過在plt.plot（）中設置color參數來更改條形的顏色。
![Alt text](resource/34_BarChart_Matplotlib-min.png){width:100px;}
---
## __F. Change__
### 35. Time Series Plot
> 時間序列圖用於可視化給定指標如何隨時間變化。 在這裡，您可以查看1949年至1969年之間的航空旅客流量變化。
![Alt text](resource/35_TimeSeries_Matplotlib-min.png){width:100px;}

### 36. Time Series with Peaks and Troughs Annotated
> 下面的時間序列繪製了所有的波峰和波谷，並註釋了選定的特殊事件的發生。
![Alt text](resource/36_TimeSeries_Peaks_Troughs_Matplotlib-min.png){width:100px;}

### 37. Autocorrelation (ACF) and Partial Autocorrelation (PACF) Plot
> ACF圖顯示了時間序列與其自身滯後的相關性。 每條垂直線（在自相關圖上）表示序列與從滯後0開始的滯後之間的相關性。圖中的藍色陰影區域是顯著性水平。 那些位於藍線上方的滯後就是巨大的滯後。那麼如何解釋呢？
> 對於AirPassengers，我們看到多達14個滯後時間已越過藍線，因此意義重大。 這意味著，距今已有14年之久的航空客運量對今天的客運量產生了影響。 另一方面，PACF顯示了任何給定的（時間序列）滯後與當前序列之間的自相關，但是去除了兩者之間的滯後。
![Alt text](resource/37_ACF_PACF_Plot_Matplotlib_Statmodels-min.png){width:100px;}

### 38. Cross Correlation plot
> 互相關圖顯示了兩個時間序列之間的時滯。
![Alt text](resource/38_CCFPlot_Statmodels_Matplotlib-min.png){width:100px;}

### 39. Time Series Decomposition Plot
> 時間序列分解圖顯示了時間序列按趨勢，季節和殘差成分的分解。
![Alt text](resource/39_TimeSeries_Decomposition_Statmodels_Matplotlib-min.png){width:100px;}

### 40. Multiple Time Series
> 您可以在同一張圖表上繪製測量同一值的多個時間序列
![Alt text](resource/40_Multiple_Timeseries_in_Same_Plot_Matplotlib-min.png){width:100px;}

### 41. Plotting with different scales using secondary Y axis
> 如果要顯示在同一時間點測量兩個不同量的兩個時間序列，則可以在右邊的第二個Y軸上再次繪製第二個序列。
![Alt text](resource/41_Timeseries_of_Different_Scales_On_Secondary_Y_Axis_Matplotlib-min.png){width:100px;}

### 42. 42. Time Series with Error Bands
> 如果您有一個在每個時間點（日期/時間戳）具有多個觀測值的時間序列數據集，則可以構建帶有誤差帶的時間序列。 您可以在下面看到一些基於一天中不同時間的訂單的示例。 另一個例子是在45天的時間內到達的訂單數量。 在這種方法中，訂單數量的平均值由白線表示。 然後計算出95％的置信帶並圍繞均值繪製。
![Alt text](resource/42_TimeSeries_with_ErrorBands_1_Matplotlib-min.png){width:100px;}


### 43. Stacked Area Chart
> 堆積面積圖直觀地表示了多個時間序列的貢獻程度，因此可以輕鬆地進行相互比較。
![Alt text](resource/43_Stacked_Area_Chart_Matplotlib-min.png){width:100px;}

### 44. Area Chart UnStacked
> 未堆疊的面積圖用於可視化兩個或多個系列相對於彼此的進度（漲跌）。 在下面的圖表中，您可以清楚地看到隨著失業時間的中位數增加，個人儲蓄率如何下降。 未堆積面積圖很好地展現了這種現象
![Alt text](resource/44_Unstacked_Area_Chart_Matplotlib-min.png){width:100px;}

### 45. Calendar Heat Map
> 日曆地圖是與時間序列相比可視化基於時間的數據的替代方法，而不是首選方法。 儘管可以在視覺上吸引人，但數值並不十分明顯。但是，它可以有效地很好地描繪出極端值和假日效果。
![Alt text](resource/45_Calendar_Heatmap_Matplotlib_Calmap-min.png){width:100px;}

### 46. Seasonal Plot
> 季節性圖可用於比較上一個季節的同一天（年/月/周等）的時間序列執行情況。
![Alt text](resource/46_Seasonal_Plot_Matplotlib-min.png){width:100px;}
---
## __G. Groups__
### 47. Dendrogram
> 樹狀圖根據給定的距離度量將相似的點組合在一起，並根據該點的相似性將它們組織成樹狀鏈接。
![Alt text](resource/47_Dendrogram_Matplotlib-min.png){width:100px;}

### 48. Cluster Plot
> 群集圖可用於劃分屬於同一群集的點。 下面是一個示例性示例，根據USArrests數據集將美國各州分為5個組。 該聚類圖使用“謀殺”和“攻擊”列作為X軸和Y軸。 或者，您可以將第一個到第一個主要成分用作X和Y軸。
![Alt text](resource/48_Cluster_Plot_Matplotlib-min.png){width:100px;}

### 49. Andrews Curve
> 安德魯斯曲線可幫助可視化是否存在基於給定分組的數字特徵的固有分組。 如果要素（數據集中的列）不能幫助區分組（圓柱），則如下圖所示，這些線將無法很好地分離。
![Alt text](resource/49_Andrews_Curves_On_Mtcars-min.png){width:100px;}

### 50. Parallel Coordinates
> 平行坐標有助於可視化某個功能是否有助於有效地隔離組。 如果實行隔離，則該功能可能對預測該組非常有用。
![Alt text](resource/50_Parallel_Coordinates_Matplotlib_Pandas-min.png){width:100px;}