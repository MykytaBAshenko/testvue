<template>
  <div class="tabelShell">

  <div class="tabel">
    <div class="tabelHead tabelGrid">
      <div>Location</div>
      <div>Temparature</div>
      <div>Rainfall</div>
      <div></div>
    </div>
    <div @click="startForecast(location.id, location.name)" v-for="location in locations" :key="location.id" class="tabelBody tabelGrid">
      <div class="first">
    <NumberImage :numberImage="location.weather.weather" /> 
    {{ location.name }}
  </div>
      <div>{{ location.weather.temperature }} C</div>
      <div>{{ location.weather.rainfall }} mm</div>
      <div class="trash"><FontAwesomeIcon  @click="deleteLocation(location.id)" :icon="['fas', 'trash']" class="trash-icon" /></div>
    </div>
  </div>
    
  </div>
  </template>
  
  <script setup>

const props = defineProps({
  locations: Array,
  deleteLocation: Function,
  startForecast: Function
});

  </script>
  
  <style scoped>
  .tabel{
    font-size: 22px;
  width: 100%;
  justify-self: center;
  max-width: 1280px;
  }
  .trash{
    justify-self: end;
  }
  .tabelHead{
    width: 100%;

    background-color: rgb(50, 50, 50);
    padding: 15px 35px;
  }
    .tabelBody{
      width: 100%;
      padding: 15px 35px;
      background-color: rgb(27 27, 29);
    }

    .tabelBody:hover{
      background-color: rgb(35, 35, 35);
      cursor: pointer;
    }
  .first{
    display: grid;
    grid-template-columns: auto 1fr;
    align-items: center;
    gap: 10px;
  }
   .tabelGrid{
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 2fr;
    align-items: center;
    justify-content: center;
   }
   .tabelShell{
    width: 100%;
    display: grid;
    }
    .trash:hover{
      color: red;
      cursor: pointer;
    }
  </style>