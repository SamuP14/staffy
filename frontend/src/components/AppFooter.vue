<script setup lang="ts">
import { BIconFacebook, BIconTwitterX, BIconLinkedin, BIconInstagram } from 'bootstrap-icons-vue';
</script>

<template>
  <footer class="footer fixed-bottom" role="contentinfo" aria-label="Footer">
    <div class="container">
      <div class="row justify-content-between align-items-center">
        <div class="col-md-6 text-md-left">
          <p class="mb-0">&copy; {{ new Date().getFullYear() }} Staffy | Easy Staff Solutions. All rights reserved.</p>
          <p class="mb-0">Making staff management simple, fast, and efficient.</p>
        </div>
        <div class="col-md-6 text-md-right">
          Follow us:
          <ul class="social-links list-unstyled mb-0" aria-label="Social media links">
            <li class="d-inline-block me-3">
              <a href="#" class="text-white d-flex align-items-center gap-2" target="_blank">
                <BIconFacebook /> Facebook
              </a>
            </li>
            <li class="d-inline-block me-3">
              <a href="#" class="text-white d-flex align-items-center gap-2" target="_blank">
                <BIconTwitterX /> Twitter
              </a>
            </li>
            <li class="d-inline-block me-3">
              <a href="#" class="text-white d-flex align-items-center gap-2" target="_blank">
                <BIconLinkedin /> LinkedIn
              </a>
            </li>
            <li class="d-inline-block">
              <a href="#" class="text-white d-flex align-items-center gap-2" target="_blank">
                <BIconInstagram /> Instagram
              </a>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </footer>
</template>

<style scoped>
.footer {
  background-color: #0D7BA6;
  color: #fff;
  text-align: center;
  padding: 1rem 0;
  width: 100vw;
}

.social-links a {
  text-decoration: none;
  color: #fff;
  font-size: 1.1rem;
}

.social-links a:hover {
  color: #0d6efd;
  background-color: transparent;
}

.social-links .bi {
  margin-right: 5px;
}

@media (max-width: 768px) {
  .social-links {
    text-align: center;
    margin-top: 10px;
  }

  .text-md-left {
    text-align: center !important;
    margin-bottom: 10px;
  }

  .text-md-right {
    text-align: center !important;
  }
}
</style>
