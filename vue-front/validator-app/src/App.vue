<template>
  <div id="app">
    <div class="container">
      <h1>KS - File validator</h1>
      <textarea v-model="text" placeholder="Paste the lyrics here..." />
      <v-btn color="error" large=true v-on:click="validate(text)"><span>Validate</span></v-btn>
      <textarea v-model="error_log" />
    </div>    
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'app',
  data () {
    return {
      text: '',
      error_log: ''
    }
  },
  methods: {
    validate: function (text) {
      axios.post("http://localhost:5000/check", {
          'lines': text.split('\n')
        })
        .then((response) => {
          this.error_log = response.data.join('\n');
          console.log(response)
        });
    }
  }
}
</script>

<style lang="scss">

#app {  
  font-family: 'Montserrat', sans-serif, 'Helvetica', 'Arial', 'sans-serif';
  background-color: black;
}

h1 {
  color: white;
}

.container {
  margin: 0 auto;
  margin-top: 50px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: black;

  max-width: 700px;
}

textarea {
  margin: 50px;
  width: 600px;
  height: 300px;
  background-color: white;
  padding: 20px;
}

button {
  background-color: #00adbc;
}

span {
  font-size: 1.3em;
}

html {
  background-color: black;
}

</style>
