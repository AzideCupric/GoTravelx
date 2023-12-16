<script setup lang="ts"></script>

<template>
  <div class="antialiased mx-auto">
    <div class="min-h-screen flex flex-col">
      <router-view :key="$route.fullPath"></router-view>
    </div>
  </div>
</template>

<style scoped></style>
