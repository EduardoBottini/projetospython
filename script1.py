import tkinter as tk
import random

BG        = "#1a1a2e"
CARD_BG   = "#16213e"
ACCENT    = "#e94560"
GREEN     = "#2ecc71"
BLUE      = "#0f3460"
ORANGE    = "#f5a623"
GRAY      = "#aaaaaa"
WHITE     = "#ffffff"
DARK_GRAY = "#666699"


def styled_btn(parent, text, color, command, pady=12, padx=0, font_size=11):
    return tk.Button(parent, text=text, font=("Segoe UI", font_size, "bold"),
                     bg=color, fg=WHITE, activebackground=color,
                     activeforeground=WHITE, relief="flat", bd=0,
                     cursor="hand2", pady=pady, padx=padx, command=command)


def label(parent, text, size=11, bold=False, color=WHITE, bg=BG, **kwargs):
    weight = "bold" if bold else "normal"
    return tk.Label(parent, text=text, font=("Segoe UI", size, weight),
                    bg=bg, fg=color, **kwargs)


class MenuPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("🎮 Mini Games")
        self.root.geometry("420x500")
        self.root.resizable(False, False)
        self.root.configure(bg=BG)
        self.frame = tk.Frame(root, bg=BG)
        self.frame.pack(expand=True, fill="both")
        self.build()

    def build(self):
        label(self.frame, "🎮 Mini Games", 28, bold=True, color=ACCENT, bg=BG).pack(pady=(50, 6))
        label(self.frame, "Escolha um jogo para começar", 11, color=GRAY, bg=BG).pack(pady=(0, 40))
        games = [
            ("🧠  Adivinhe o Número", ACCENT,   self.open_adivinhar),
            ("🃏  Blackjack",         "#7c3aed", self.open_blackjack),
        ]
        for text, color, cmd in games:
            styled_btn(self.frame, text, color, cmd, pady=16, padx=40, font_size=13).pack(fill="x", padx=60, pady=10)
        label(self.frame, "© 2026 Mini Games", 8, color=DARK_GRAY, bg=BG).pack(side="bottom", pady=12)

    def _switch(self, GameClass):
        self.frame.pack_forget()
        game_frame = tk.Frame(self.root, bg=BG)
        game_frame.pack(expand=True, fill="both")
        def back():
            game_frame.destroy()
            self.frame.pack(expand=True, fill="both")
            self.root.geometry("420x500")
            self.root.title("🎮 Mini Games")
        GameClass(game_frame, self.root, back)

    def open_adivinhar(self): self._switch(AdivinharNumero)
    def open_blackjack(self): self._switch(Blackjack)


class AdivinharNumero:
    def __init__(self, frame, root, back_cb):
        self.frame   = frame
        self.root    = root
        self.back_cb = back_cb
        root.title("🧠 Adivinhe o Número")
        root.geometry("420x600")
        self.build_ui()
        self.init_game()

    def build_ui(self):
        top = tk.Frame(self.frame, bg=BG)
        top.pack(fill="x", padx=20, pady=(16, 0))
        styled_btn(top, "← Voltar", BLUE, self.back_cb, pady=6, padx=10, font_size=9).pack(side="left")
        label(self.frame, "🧠 Adivinhe!", 24, bold=True, color=ACCENT, bg=BG).pack(pady=(6, 2))
        label(self.frame, "Pense em um número de 0 a 100 e responda!", 9, color=GRAY, bg=BG).pack()

        self.card = tk.Frame(self.frame, bg=CARD_BG)
        self.card.pack(padx=30, fill="x", pady=12)

        self.guess_lbl = label(self.card, "50", 64, bold=True, color=ACCENT, bg=CARD_BG)
        self.guess_lbl.pack(pady=(18, 0))
        self.range_lbl = label(self.card, "Intervalo: 0 — 100", 9, color=DARK_GRAY, bg=CARD_BG)
        self.range_lbl.pack()

        bar_f = tk.Frame(self.card, bg=CARD_BG)
        bar_f.pack(fill="x", padx=24, pady=(6, 12))
        self.bar_bg   = tk.Canvas(bar_f, height=8, bg=BLUE, highlightthickness=0)
        self.bar_bg.pack(fill="x")
        self.bar_fill = self.bar_bg.create_rectangle(0, 0, 0, 8, fill=ACCENT, outline="")

        self.att_lbl = label(self.card, "Tentativa 1 de 10", 10, bold=True, color=ORANGE, bg=CARD_BG)
        self.att_lbl.pack()
        self.msg_lbl = label(self.card, "", 11, color=WHITE, bg=CARD_BG, wraplength=340, justify="center")
        self.msg_lbl.pack(pady=(6, 16))

        btn_f = tk.Frame(self.card, bg=CARD_BG)
        btn_f.pack(padx=16, fill="x", pady=(0, 10))
        styled_btn(btn_f, "⬇ Menor",    BLUE,   lambda: self.respond("menor")).grid(row=0, column=0, padx=(0, 4), sticky="ew")
        styled_btn(btn_f, "✅ Acertei!", GREEN,  lambda: self.respond("acertei")).grid(row=0, column=1, padx=4, sticky="ew")
        styled_btn(btn_f, "⬆ Maior",    ACCENT, lambda: self.respond("maior")).grid(row=0, column=2, padx=(4, 0), sticky="ew")
        for c in range(3): btn_f.columnconfigure(c, weight=1)

        self.hist_lbl = label(self.card, "", 8, color=DARK_GRAY, bg=CARD_BG, wraplength=340, justify="center")
        self.hist_lbl.pack(pady=(8, 12))

        self.res_frame = tk.Frame(self.frame, bg=BG)
        self.res_emoji = label(self.res_frame, "", 52, bg=BG)
        self.res_emoji.pack(pady=(30, 4))
        self.res_title = label(self.res_frame, "", 20, bold=True, bg=BG)
        self.res_title.pack()
        self.res_sub = label(self.res_frame, "", 10, color=GRAY, bg=BG, wraplength=340, justify="center")
        self.res_sub.pack(pady=(6, 24))
        styled_btn(self.res_frame, "🔄 Jogar Novamente", GREEN, self.restart, pady=12, padx=30).pack()
        styled_btn(self.res_frame, "← Menu", BLUE, self.back_cb, pady=8, padx=20, font_size=9).pack(pady=(10, 0))

    def init_game(self):
        self.low, self.high = 0, 100
        self.attempt = 1
        self.history = []
        self.current = (self.low + self.high) // 2
        self.res_frame.pack_forget()
        self.card.pack(padx=30, fill="x", pady=12)
        self.update_ui()

    def update_ui(self):
        self.guess_lbl.config(text=str(self.current))
        self.range_lbl.config(text=f"Intervalo: {self.low} — {self.high}")
        self.att_lbl.config(text=f"Tentativa {self.attempt} de 10")
        msgs = ["Esse é o número que você pensou?", "Quente ou frio? 🤔",
                "Estou chegando perto...", "Sinto que sei! 🔥", "Quase lá... 🎯"]
        self.msg_lbl.config(text=msgs[min(self.attempt - 1, 4)])
        self.bar_bg.update_idletasks()
        w = self.bar_bg.winfo_width()
        self.bar_bg.coords(self.bar_fill, 0, 0, max(((self.high - self.low) / 100) * w, 6), 8)
        hist = "  ".join(f"{h['g']}{'⬆' if h['a'] == 'maior' else '⬇'}" for h in self.history)
        self.hist_lbl.config(text=f"Histórico: {hist}" if hist else "")

    def respond(self, ans):
        if ans == "acertei":
            self._show_result(True)
            return
        self.history.append({"g": self.current, "a": ans})
        if ans == "maior": self.low  = self.current + 1
        else:              self.high = self.current - 1
        self.attempt += 1
        if self.attempt > 10 or self.low > self.high:
            self._show_result(False)
            return
        self.current = (self.low + self.high) // 2
        self.update_ui()

    def _show_result(self, won):
        self.card.pack_forget()
        self.res_frame.pack(expand=True, fill="both")
        if won:
            self.res_emoji.config(text="🎉")
            self.res_title.config(text="Acertei!", fg=GREEN)
            self.res_sub.config(text=f"Descobri o número {self.current} em {self.attempt} tentativa{'s' if self.attempt > 1 else ''}!")
        else:
            self.res_emoji.config(text="😅")
            self.res_title.config(text="Não consegui!", fg=ACCENT)
            self.res_sub.config(text="Você me enganou! 🤫")

    def restart(self):
        self.init_game()


NAIPES  = ["♠", "♥", "♦", "♣"]
VALORES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


def novo_baralho():
    return [(v, n) for n in NAIPES for v in VALORES]

def valor_carta(c):
    v = c[0]
    if v in ("J", "Q", "K"): return 10
    if v == "A":              return 11
    return int(v)

def valor_mao(mao):
    total = sum(valor_carta(c) for c in mao)
    ases  = sum(1 for c in mao if c[0] == "A")
    while total > 21 and ases:
        total -= 10
        ases  -= 1
    return total

def carta_str(c):
    naipe = c[1]
    cor   = "#ff4444" if naipe in ("♥", "♦") else WHITE
    return f"{c[0]}{c[1]}", cor


class Blackjack:
    def __init__(self, frame, root, back_cb):
        self.frame   = frame
        self.root    = root
        self.back_cb = back_cb
        self.saldo   = 1000
        self.aposta  = 0
        root.title("🃏 Blackjack")
        root.geometry("420x680")
        self.build_ui()
        self.tela_aposta()

    def build_ui(self):
        top = tk.Frame(self.frame, bg=BG)
        top.pack(fill="x", padx=20, pady=(16, 0))
        styled_btn(top, "← Voltar", BLUE, self.back_cb, pady=6, padx=10, font_size=9).pack(side="left")
        self.saldo_lbl = label(top, f"💰 R$ {self.saldo}", 11, bold=True, color=ORANGE, bg=BG)
        self.saldo_lbl.pack(side="right")

        label(self.frame, "🃏 Blackjack", 24, bold=True, color="#7c3aed", bg=BG).pack(pady=(4, 2))

        self.game_frame = tk.Frame(self.frame, bg=BG)
        self.game_frame.pack(fill="both", expand=True, padx=20)

        label(self.game_frame, "DEALER", 9, bold=True, color=DARK_GRAY, bg=BG).pack(anchor="w")
        self.dealer_frame = tk.Frame(self.game_frame, bg=BG)
        self.dealer_frame.pack(fill="x", pady=(2, 0))
        self.dealer_val = label(self.game_frame, "", 10, color=GRAY, bg=BG)
        self.dealer_val.pack(anchor="w")

        tk.Frame(self.game_frame, bg=DARK_GRAY, height=1).pack(fill="x", pady=8)

        label(self.game_frame, "VOCÊ", 9, bold=True, color=DARK_GRAY, bg=BG).pack(anchor="w")
        self.player_frame = tk.Frame(self.game_frame, bg=BG)
        self.player_frame.pack(fill="x", pady=(2, 0))
        self.player_val = label(self.game_frame, "", 10, color=GRAY, bg=BG)
        self.player_val.pack(anchor="w")

        self.result_lbl = label(self.game_frame, "", 16, bold=True, color=WHITE, bg=BG)
        self.result_lbl.pack(pady=(10, 0))

        self.action_frame = tk.Frame(self.game_frame, bg=BG)
        self.action_frame.pack(fill="x", pady=8)

        self.btn_hit    = styled_btn(self.action_frame, "🃏 Pedir",  GREEN,  self.hit,    pady=10)
        self.btn_stand  = styled_btn(self.action_frame, "✋ Parar",  ACCENT, self.stand,  pady=10)
        self.btn_double = styled_btn(self.action_frame, "⚡ Dobrar", ORANGE, self.double, pady=10)

        self.btn_hit.grid(row=0, column=0, padx=(0, 4), sticky="ew")
        self.btn_stand.grid(row=0, column=1, padx=4, sticky="ew")
        self.btn_double.grid(row=0, column=2, padx=(4, 0), sticky="ew")
        for c in range(3): self.action_frame.columnconfigure(c, weight=1)

        self.btn_nova = styled_btn(self.game_frame, "🔄 Nova Rodada", "#7c3aed", self.tela_aposta, pady=10)
        self.btn_nova.pack(fill="x", pady=(4, 0))

        self.bet_frame = tk.Frame(self.frame, bg=BG)
        label(self.bet_frame, "💰 Faça sua aposta", 16, bold=True, color=ORANGE, bg=BG).pack(pady=(20, 16))

        chips = [(50, "#555"), (100, BLUE), (200, "#7c3aed"), (500, ACCENT)]
        chip_row = tk.Frame(self.bet_frame, bg=BG)
        chip_row.pack()
        for val, cor in chips:
            styled_btn(chip_row, f"R${val}", cor,
                       lambda v=val: self.add_aposta(v), pady=10, padx=4, font_size=10).pack(side="left", padx=6)

        self.aposta_lbl = label(self.bet_frame, "Aposta: R$ 0", 14, bold=True, color=WHITE, bg=BG)
        self.aposta_lbl.pack(pady=(16, 4))

        row2 = tk.Frame(self.bet_frame, bg=BG)
        row2.pack(pady=4)
        styled_btn(row2, "Limpar",   GRAY,  self.limpar_aposta,  pady=8, padx=16, font_size=10).pack(side="left", padx=6)
        styled_btn(row2, "▶  Jogar", GREEN, self.iniciar_rodada, pady=8, padx=20, font_size=11).pack(side="left", padx=6)

    def tela_aposta(self):
        self.game_frame.pack_forget()
        self.aposta = 0
        self.aposta_lbl.config(text="Aposta: R$ 0")
        self.bet_frame.pack(fill="both", expand=True, padx=20)
        self.result_lbl.config(text="")

    def add_aposta(self, v):
        if self.aposta + v <= self.saldo:
            self.aposta += v
            self.aposta_lbl.config(text=f"Aposta: R$ {self.aposta}")

    def limpar_aposta(self):
        self.aposta = 0
        self.aposta_lbl.config(text="Aposta: R$ 0")

    def iniciar_rodada(self):
        if self.aposta == 0:
            self.aposta_lbl.config(text="⚠ Faça uma aposta!", fg=ACCENT)
            return
        self.bet_frame.pack_forget()
        self.game_frame.pack(fill="both", expand=True, padx=20)

        self.baralho     = novo_baralho()
        random.shuffle(self.baralho)
        self.mao_dealer  = [self.baralho.pop(), self.baralho.pop()]
        self.mao_jogador = [self.baralho.pop(), self.baralho.pop()]

        self.saldo -= self.aposta
        self.saldo_lbl.config(text=f"💰 R$ {self.saldo}")
        self.result_lbl.config(text="")

        self._set_buttons(True)
        self.btn_double.config(state="normal" if self.saldo >= self.aposta else "disabled")
        self.btn_nova.pack_forget()

        self.render_maos(esconder_dealer=True)

        if valor_mao(self.mao_jogador) == 21:
            self.finalizar()

    def hit(self):
        self.mao_jogador.append(self.baralho.pop())
        self.render_maos(esconder_dealer=True)
        if valor_mao(self.mao_jogador) >= 21:
            self.finalizar()

    def stand(self):
        self.finalizar()

    def double(self):
        self.saldo  -= self.aposta
        self.aposta *= 2
        self.saldo_lbl.config(text=f"💰 R$ {self.saldo}")
        self.mao_jogador.append(self.baralho.pop())
        self.render_maos(esconder_dealer=True)
        self.finalizar()

    def finalizar(self):
        while valor_mao(self.mao_dealer) < 17:
            self.mao_dealer.append(self.baralho.pop())

        self.render_maos(esconder_dealer=False)
        self._set_buttons(False)

        pj = valor_mao(self.mao_jogador)
        pd = valor_mao(self.mao_dealer)

        if pj > 21:
            msg, cor, ganho = "💥 Estourou! Você perdeu.", ACCENT, 0
        elif pd > 21 or pj > pd:
            bonus = 2.5 if pj == 21 and len(self.mao_jogador) == 2 else 2
            ganho = int(self.aposta * bonus)
            msg   = f"🎉 Você ganhou R$ {ganho}!" if bonus == 2 else f"🌟 Blackjack! +R$ {ganho}!"
            cor   = GREEN
            self.saldo += ganho
        elif pj == pd:
            ganho = self.aposta
            msg, cor = "🤝 Empate! Aposta devolvida.", ORANGE
            self.saldo += ganho
        else:
            msg, cor, ganho = "😞 Dealer venceu.", ACCENT, 0

        self.saldo_lbl.config(text=f"💰 R$ {self.saldo}")
        self.result_lbl.config(text=msg, fg=cor)
        self.btn_nova.pack(fill="x", pady=(4, 0))

        if self.saldo == 0:
            self.result_lbl.config(text="💸 Sem saldo! Reiniciando...", fg=ACCENT)
            self.frame.after(2000, self._reset_saldo)

    def _reset_saldo(self):
        self.saldo = 1000
        self.saldo_lbl.config(text=f"💰 R$ {self.saldo}")
        self.tela_aposta()

    def render_maos(self, esconder_dealer):
        for w in self.dealer_frame.winfo_children(): w.destroy()
        for w in self.player_frame.winfo_children(): w.destroy()

        for i, c in enumerate(self.mao_dealer):
            if i == 1 and esconder_dealer:
                self._carta_widget(self.dealer_frame, "🂠", WHITE)
            else:
                txt, cor = carta_str(c)
                self._carta_widget(self.dealer_frame, txt, cor)

        dv = valor_mao([self.mao_dealer[0]]) if esconder_dealer else valor_mao(self.mao_dealer)
        self.dealer_val.config(text=f"Valor: {dv}{'+ ?' if esconder_dealer else ''}")

        for c in self.mao_jogador:
            txt, cor = carta_str(c)
            self._carta_widget(self.player_frame, txt, cor)
        self.player_val.config(text=f"Valor: {valor_mao(self.mao_jogador)}")

    def _carta_widget(self, parent, text, color):
        f = tk.Frame(parent, bg=WHITE, bd=0, relief="flat",
                     highlightbackground="#cccccc", highlightthickness=1)
        f.pack(side="left", padx=3, pady=2)
        tk.Label(f, text=text, font=("Segoe UI", 13, "bold"),
                 bg=WHITE, fg=color, width=4, pady=6).pack()

    def _set_buttons(self, active):
        state = "normal" if active else "disabled"
        for b in (self.btn_hit, self.btn_stand, self.btn_double):
            b.config(state=state)


if __name__ == "__main__":
    root = tk.Tk()
    MenuPrincipal(root)
    root.mainloop()