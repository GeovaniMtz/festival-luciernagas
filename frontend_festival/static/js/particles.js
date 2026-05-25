(function () {

  const canvas = document.getElementById('particlesCanvas');

  if (!canvas) return;

  const ctx = canvas.getContext('2d');

  function resize() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  }

  resize();

  window.addEventListener('resize', resize);

  const COLORS = [
    '#A3E635',
    '#FEE715',
    '#4ECBA5',
    '#22C55E',
    '#E8F94A'
  ];

  function rand(min, max) {
    return Math.random() * (max - min) + min;
  }

  class Particle {

    constructor() {
      this.reset();
    }

    reset() {

      this.x = rand(0, canvas.width);
      this.y = rand(0, canvas.height);

      this.size = rand(1.5, 3.5);

      this.vx = rand(-0.5, 0.5);
      this.vy = rand(-0.25, 0.25);

      this.color =
        COLORS[Math.floor(Math.random() * COLORS.length)];

      this.maxA = rand(0.35, 0.85);

      this.life = rand(120, 260);

      this.age = 0;

      this.ps = rand(0.02, 0.05);

      this.po = rand(0, Math.PI * 2);

      this.a = 0;
    }

    update() {

      this.age++;

      this.x += this.vx;
      this.y += this.vy;

      /* Movimiento orgánico */
      this.x += Math.sin(
        this.age * 0.02 + this.po
      ) * 0.15;

      const half = this.life / 2;

      const base =
        this.age < half
          ? (this.age / half) * this.maxA
          : ((this.life - this.age) / half) * this.maxA;

      this.a = Math.max(
        0,
        Math.min(
          1,
          base + Math.sin(this.age * this.ps + this.po) * 0.15
        )
      );

      if (this.age >= this.life) {
        this.reset();
      }
    }

    draw() {

      ctx.save();

      ctx.globalAlpha = this.a;

      const g = ctx.createRadialGradient(
        this.x,
        this.y,
        0,
        this.x,
        this.y,
        this.size * 4
      );

      g.addColorStop(0, this.color);
      g.addColorStop(1, 'transparent');

      ctx.fillStyle = g;

      ctx.beginPath();

      ctx.arc(
        this.x,
        this.y,
        this.size * 4,
        0,
        Math.PI * 2
      );

      ctx.fill();

      ctx.globalAlpha = Math.min(1, this.a * 1.8);

      ctx.fillStyle = '#fff';

      ctx.beginPath();

      ctx.arc(
        this.x,
        this.y,
        this.size * 0.5,
        0,
        Math.PI * 2
      );

      ctx.fill();

      ctx.restore();
    }
  }

  const particles = Array.from(
    { length: 85 },
    () => new Particle()
  );

  function animate() {

    ctx.clearRect(
      0,
      0,
      canvas.width,
      canvas.height
    );

    particles.forEach(p => {
      p.update();
      p.draw();
    });

    requestAnimationFrame(animate);
  }

  animate();

})();