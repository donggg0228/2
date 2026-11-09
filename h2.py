import cv2


def blur_roi(img, ymin, ymax, xmin, xmax, ksize=(99, 99)):
    """
    僅對指定 ROI 區域進行高斯模糊，其他區域保持原樣
    """
    result = img.copy()
    roi = result[ymin:ymax, xmin:xmax]
    # 高斯模糊 (核大小須為奇數，數值愈大愈模糊)
    blurred_roi = cv2.GaussianBlur(roi, ksize, 0)
    result[ymin:ymax, xmin:xmax] = blurred_roi
    return result


def main():
    # =========================================================
    # 1. 處理 VESPA.tif (車牌號碼：LQY-888)
    # =========================================================
    vespa_img = cv2.imread('VESPA.tif')
    if vespa_img is None:
        print("【錯誤】找不到 VESPA.tif，請確認圖檔已放置於專案根目錄下！")
    else:
        h, w = vespa_img.shape[:2]

        # 精準涵蓋 VESPA 側轉車牌 LQY-888 區域 (單位：像素百分比)
        ymin, ymax = int(h * 0.76), int(h * 0.98)
        xmin, xmax = int(w * 0.17), int(w * 0.57)

        vespa_result = blur_roi(vespa_img, ymin, ymax, xmin, xmax, ksize=(201, 201))

        # 儲存與顯示結果
        cv2.imwrite('VESPA_blurred.jpg', vespa_result)
        cv2.imshow('1. VESPA - Blurred (LQY-888)', vespa_result)
        print("✔ VESPA.tif 處理完畢，已成功儲存為 VESPA_blurred.jpg")

    # =========================================================
    # 2. 處理 BMW X2.tif (車牌號碼：BTG-1528)
    # =========================================================
    bmw_img = cv2.imread('BMW X2.tif')
    if bmw_img is None:
        print("【錯誤】找不到 BMW X2.tif，請確認圖檔已放置於專案根目錄下！")
    else:
        h, w = bmw_img.shape[:2]

        # 精準涵蓋 BMW X2 前保桿車牌 BTG-1528 區域
        ymin, ymax = int(h * 0.73), int(h * 0.83)
        xmin, xmax = int(w * 0.04), int(w * 0.12)

        bmw_result = blur_roi(bmw_img, ymin, ymax, xmin, xmax, ksize=(51, 51))

        # 儲存與顯示結果
        cv2.imwrite('BMW_X2_blurred.jpg', bmw_result)
        cv2.imshow('2. BMW X2 - Blurred (BTG-1528)', bmw_result)
        print("✔ BMW X2.tif 處理完畢，已成功儲存為 BMW_X2_blurred.jpg")

    # =========================================================
    # 3. 保持視窗顯示，直到按下任意鍵
    # =========================================================
    print("所有影像處理完畢！請在跳出的影像預覽視窗中按任意鍵關閉...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()