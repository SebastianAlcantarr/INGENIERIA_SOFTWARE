<template>
  <div class="min-h-screen bg-slate-900 text-slate-100">
    <header
      class="sticky top-0 z-10 bg-slate-900/60 backdrop-blur border-b border-white/10"
    >
      <div
        class="max-w-5xl mx-auto px-4 py-3 flex items-center justify-between"
      >
        <h1 class="text-base sm:text-lg font-semibold tracking-tight"></h1>
      </div>
    </header>

    <main class="max-w-5xl px-4 py-10">
      <section
        class="rounded-3xl ring-1 ring-white/10 p-6 sm:p-8 shadow-xl shadow-black/20"
      >
        <h2 class="text-2xl sm:text-3xl font-bold">Bienvenido</h2>
        <p class="mt-2 text-slate-300 leading-relaxed">
          Interfaz para derivar
        </p>

        <div class="mt-6 flex flex-wrap gap-3">
          <a
            class="inline-flex h-12 w-12 items-center justify-center rounded-full bg-white/10 hover:bg-white/20 ring-1 ring-white/10 transition-transform duration-200 hover:scale-105"
            href="https://www.twitch.tv/"
            target="_blank"
          >
            <svg width="28" height="28">
              <use href="/sprite.svg#twitch"></use>
            </svg>
          </a>
          <a
            class="inline-flex h-12 w-12 items-center justify-center rounded-full bg-white/10 hover:bg-white/20 ring-1 ring-white/10 transition-transform duration-200 hover:scale-105"
            href="https://www.instagram.com/"
            target="_blank"
          >
            <svg width="28" height="28">
              <use href="/sprite.svg#instagram"></use>
            </svg>
          </a>
          <a
            class="inline-flex h-12 w-12 items-center justify-center rounded-full bg-white/10 hover:bg-white/20 ring-1 ring-white/10 transition-transform duration-200 hover:scale-105"
            href="https://www.linkedin.com/"
            target="_blank"
          >
            <svg width="28" height="28">
              <use href="/sprite.svg#linkedin"></use>
            </svg>
          </a>
          <a
            class="inline-flex h-12 w-12 items-center justify-center rounded-full bg-white/10 hover:bg-white/20 ring-1 ring-white/10 transition-transform duration-200 hover:scale-105"
            href="https://www.youtube.com/"
            target="_blank"
          >
            <svg width="28" height="28">
              <use href="/sprite.svg#youtube"></use>
            </svg>
          </a>
          <a
            class="inline-flex h-12 w-12 items-center justify-center rounded-full bg-white/10 hover:bg-white/20 ring-1 ring-white/10 transition-transform duration-200 hover:scale-105"
            href="https://x.com/"
            target="_blank"
          >
            <svg width="28" height="28"><use href="/sprite.svg#x"></use></svg>
          </a>
          <a
            class="inline-flex h-12 w-12 items-center justify-center rounded-full bg-white/10 hover:bg-white/20 ring-1 ring-white/10 transition-transform duration-200 hover:scale-105"
            href="https://github.com/"
            target="_blank"
          >
            <svg width="28" height="28">
              <use href="/sprite.svg#github"></use>
            </svg>
          </a>
        </div>
      </section>
    </main>

    <footer class="py-8 text-center text-xs text-slate-400">© 2025</footer>
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      contador: 0,
    };
  },
};
</script>
