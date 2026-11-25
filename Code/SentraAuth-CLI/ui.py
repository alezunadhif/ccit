from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

WARNA_SUKSES = "bold green"
WARNA_GAGAL = "bold red"
WARNA_WARNING = "bold yellow"
WARNA_INFO = "bold cyan"
WARNA_JUDUL = "bold magenta"


def banner():
    """Banner ASCII ditampilkan sekali saat aplikasi pertama kali dibuka."""
    teks_banner = r"""
   _____            __           ___         __  __
  / ___/___  ____  / /__________/   | __  __/ /_/ /_
  \__ \/ _ \/ __ \/ __/ ___/ __/ /| |/ / / / __/ __ \
 ___/ /  __/ / / / /_/ /  / /_/ ___ / /_/ / /_/ / / /
/____/\___/_/ /_/\__/_/   \__/_/  |_\__,_/\__/_/ /_/
    """
    console.print(teks_banner, style=WARNA_JUDUL)
    console.print("Hardened Authentication & Access Control CLI", style="dim italic")
    console.print("=" * 62, style="dim")


def print_success(pesan: str):
    console.print(f"[✓] {pesan}", style=WARNA_SUKSES)


def print_error(pesan: str):
    console.print(f"[✗] {pesan}", style=WARNA_GAGAL)


def print_warning(pesan: str):
    console.print(f"[!] {pesan}", style=WARNA_WARNING)


def print_info(pesan: str):
    console.print(f"[i] {pesan}", style=WARNA_INFO)


def judul_bagian(teks: str):
    """Kotak judul buat tiap bagian menu."""
    console.print(Panel(teks, style=WARNA_JUDUL, expand=False))


def tabel_akun(daftar_akun: list):
    table = Table(title="Daftar Akun Sistem", show_lines=False)
    table.add_column("No", style="dim", width=4)
    table.add_column("Username", style="bold")
    table.add_column("Role")

    for i, akun in enumerate(daftar_akun, 1):
        role = akun['role_name'].upper()
        warna_role = "bold red" if role == "ADMIN" else "bold blue"
        table.add_row(str(i), akun['username'], f"[{warna_role}]{role}[/{warna_role}]")

    console.print(table)


def tabel_audit_log(logs: list):
    table = Table(title="Audit Log", show_lines=False)
    table.add_column("Waktu", style="dim")
    table.add_column("Username")
    table.add_column("Event")
    table.add_column("Status")

    warna_status = {
        "success": "bold green",
        "failed": "bold red",
        "locked": "bold yellow"
    }

    for log in logs:
        waktu = log['created_at'].strftime("%Y-%m-%d %H:%M:%S")
        username = log['username'] if log['username'] else "-"
        status = log['status']
        warna = warna_status.get(status, "white")
        table.add_row(waktu, username, log['event_type'], f"[{warna}]{status.upper()}[/{warna}]")

    console.print(table)


def tabel_menu(menu_tersedia: list):
    console.print("[bold]0.[/bold] Logout", style="white")
    for i, (kode, label) in enumerate(menu_tersedia, 1):
        console.print(f"[bold]{i}.[/bold] {label}")