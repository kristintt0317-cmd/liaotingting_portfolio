
const observer = new IntersectionObserver((entries)=>{
  entries.forEach(entry=>{
    if(entry.isIntersecting){
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);
    }
  });
}, {threshold: .12});

document.querySelectorAll('.reveal').forEach(el => observer.observe(el));

const lightbox = document.getElementById('lightbox');
const lightboxImage = document.getElementById('lightboxImage');
const closeLightbox = document.getElementById('closeLightbox');
if(lightbox && lightboxImage && closeLightbox){
  document.querySelectorAll('[data-full]').forEach(img=>{
    img.addEventListener('click', ()=>{
      lightboxImage.src = img.dataset.full;
      lightbox.classList.add('open');
      lightbox.setAttribute('aria-hidden', 'false');
    });
  });
  function closeBox(){
    lightbox.classList.remove('open');
    lightbox.setAttribute('aria-hidden', 'true');
    lightboxImage.src = '';
  }
  closeLightbox.addEventListener('click', closeBox);
  lightbox.addEventListener('click', (e)=>{ if(e.target === lightbox) closeBox(); });
  document.addEventListener('keydown', (e)=>{ if(e.key === 'Escape') closeBox(); });
}
