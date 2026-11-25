#include <stdio.h>

int main() {
    int pilihan_paket;
    float berat, total;
    char menu;

    do {
        printf("===== MENU UTAMA =====\n");
        printf("A. Lihat paket cuci\n");
        printf("B. Cek harga\n");
        printf("======================\n");
        printf("Pilih menu (A/B): ");
        scanf(" %c", &menu);

        if (menu == 'A' || menu == 'a') {
            printf("\n--- Daftar Paket Cuci ---\n");
            printf("1. Komplit 3 hari  - Rp. 6000/kg\n");
            printf("2. Komplit 2 hari  - Rp. 5000/kg\n");
            printf("3. Komplit 1 hari  - Rp. 7000/kg\n");
            printf("4. Cuci saja       - Rp. 4500/kg\n");
            printf("5. Setrika saja    - Rp. 4000/kg\n");
            printf("--------------------------\n\n");

        } else if (menu == 'B' || menu == 'b') {
            printf("\n--- Cek Harga Laundry ---\n");
            printf("Masukkan nomor paket: ");
            scanf("%d", &pilihan_paket);
            printf("Masukkan berat pakaian (kg): ");
            scanf("%f", &berat);

            switch (pilihan_paket) {
                case 1:
                    total = berat * 6000;
                    printf("Total harga: Rp. %.0f\n", total);
                    break;
                case 2:
                    total = berat * 5000;
                    printf("Total harga: Rp. %.0f\n", total);
                    break;
                case 3:
                    total = berat * 7000;
                    printf("Total harga: Rp. %.0f\n", total);
                    break;
                case 4:
                    total = berat * 4500;
                    printf("Total harga: Rp. %.0f\n", total);
                    break;
                case 5:
                    total = berat * 4000;
                    printf("Total harga: Rp. %.0f\n", total);
                    break;
                default:
                    printf("Nomor paket tidak valid!\n");
            }
            printf("\n");

        } else {
            printf("Menu tidak valid!\n\n");
        }

    } while (1); // biar looping terus sampai user close manual (Ctrl + C)

    return 0;
}
