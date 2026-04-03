# JuiChun_Colony_Counter

基於網頁技術與電腦視覺的自動化菌落計數系統 (Colony Counter)。

## 專案概述

本專案旨在提供一個輕量、精準且易於操作的工具，協助研究人員自動化計算培养皿上的菌落數量。系統採用自適應二值化 (Adaptive Thresholding) 與距離轉換 (Distance Transform) 演算法，能有效處理光線不均勻、菌落重疊等複雜情境。

## 核心功能

- **高效檢測演算法**：結合自適應對比度感應與距離轉換，精確分離並識別菌落。
- **直覺式互動介面**：
  - **ROI 編輯**：可自由調整培養皿的圓形遮罩範圍（位置與大小）。
  - **手動修正**：支援一鍵新增、刪除標記，並具備橡皮擦模式。
  - **調試模式 (Debug Mode)**：即時檢視二值化圖層，優化參數設定。
- **多樣化匯出**：
  - **數據匯出**：支援將計數結果匯出為 CSV 檔案。
  - **圖像存檔**：支援下載帶有標記的二值化或原始圖像。
- **高效能處理**：完全於瀏覽器端運行，保護數據隱私且無需安裝額外後端環境。

## 使用說明

1. **上傳影像**：點擊「Add Images」按鈕選擇培养皿照片。
2. **調整 ROI**：點擊「Move/Resize Mask」確保遮罩準確覆蓋培養皿。
3. **優化參數**：
   - 調整 **Adaptive Sens.** 以處理對比度差異。
   - 調整 **Min Peak Height** 排除背景雜訊。
   - 調整 **Split Distance** 處理菌落叢聚。
4. **人工修正**：如有漏判或誤判，可直接點擊影像進行標記，或長按 `Ctrl` 使用橡皮擦。
5. **匯出結果**：確認無誤後點擊「CSV」或「Image」按鈕存檔。

## 技術棧

- **Frontend**: Vanilla JavaScript / HTML5 / CSS3
- **CV Logic**: Integral Image / Adaptive Thresholding / Distance Transform (Optimized for Web)

## 聯絡資訊

開發者：JuiChun
Email: allenphant11@gmail.com
