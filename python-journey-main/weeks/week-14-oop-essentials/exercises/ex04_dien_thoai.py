"""Exercise: class DienThoai and two phone objects."""


class DienThoai:
    """Store and display information about a mobile phone."""

    def __init__(
        self,
        MaMay: str,
        TenMay: str,
        HangSanXuat: str,
        DungLuongPin: int,
        GiaBan: int,
    ) -> None:
        self.MaMay = MaMay
        self.TenMay = TenMay
        self.HangSanXuat = HangSanXuat
        self.DungLuongPin = DungLuongPin
        self.GiaBan = GiaBan

    def thongtindienthoai(self) -> None:
        """Display all phone information."""
        print(f"Ma may: {self.MaMay}")
        print(f"Ten may: {self.TenMay}")
        print(f"Hang san xuat: {self.HangSanXuat}")
        print(f"Dung luong pin: {self.DungLuongPin} mAh")
        print(f"Gia ban: {self.GiaBan:,} VND".replace(",", "."))
        print("-" * 40)


def main() -> None:
    """Create and display two phone objects."""
    DT01 = DienThoai("DT01", "iPhone 15 Pro", "Apple", 3274, 28990000)
    DT02 = DienThoai("DT02", "Galaxy S24 Ultra", "Samsung", 5000, 29990000)

    DT01.thongtindienthoai()
    DT02.thongtindienthoai()


if __name__ == "__main__":
    main()
