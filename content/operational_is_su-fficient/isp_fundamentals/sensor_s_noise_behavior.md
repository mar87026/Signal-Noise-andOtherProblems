# Sensor’s Noise Behavior

*What’s happened in the sensor side?*

| Sensor problem | Madarin | English |
| --- | --- | --- |
| Quantum efficiency (QE) | 光子打到感光元件上而產生電子，這就是光電效應；光產電的效率即是量子效率。偏折角度大的藍紫光會好好進到感應區，偏折角度小的會戳進另一格，變得紅光就是容易色散，因此力道小；另外是，波長越長頻率越低能量越低，所以紅光比起綠藍光QE效率較低，SNR也比較差 |  |

| Sensor Noise type | Madarin | English |
| --- | --- | --- |
| Optical black Noise | 電子流造成，全位置的錯位，會在整個感測器上造成offset，會由沒使用到的區域回報適合裁減的數值 |  |
| Dark Current Noise | 由曝光時早成的熱噪產生，曝光時間越長DCN越大；導致無光時也有雜訊，且是部分區域正常、部分地方出現隨溫度上升更趨明顯的DCN，且是隨機出現不會固定出現在一個點。 |  |
| Defect Pixel | 壞點，固定位置的雜訊。由感測器部分點數壞掉造成，這壞掉可能由輻射、製程過程、老化造成。無論任何亮度皆固定反應，或是隨機變化不隨環境變化 |  |
| Fixed Noise | 固定位置的雜訊，出現在製程瑕疵或是感測器出場久了的老化導致對於光線不一致的反應 |  |
| Read Noise | 跟位置無關，容易出現在暗部，是將類比訊號轉換為數位時的差異，因為感測器對暗與亮的處理不會比中間區段優秀(OECF) |  |
| Shot Noise | 每個時間的光都無限週期，光子落在感測器上也是隨機狀態，因此造成Poisson Distribution分布的Shot noise |  |