<template>
  <div class="table-responsive" style="margin: 0; padding: 0">
    <table class="table">
      <thead class="bg-dark text-white">
        <tr>
          <th scope="col">Code</th>
          <th scope="col">Name</th>
          <th scope="col">Open</th>
          <th scope="col">High</th>
          <th scope="col">Low</th>
          <th scope="col">Close</th>
        </tr>
      </thead>
      <tbody v-if="equities && equities.length">
        <tr :class="[parseFloat(equity.close) > parseFloat(equity.open) ? 'table-success' : parseFloat(equity.close) < parseFloat(equity.open) ? 'table-danger' : 'table-warning']" v-for="equity in [...equities].slice((currentPage-1)*20, (currentPage)*20)" :key="equity.code">
          <th scope="row">{{ equity.code }}</th>
          <td>{{ equity.name }}</td>
          <td>{{ equity.open }}</td>
          <td>{{ equity.high }}</td>
          <td>{{ equity.low }}</td>
          <td>{{ equity.close }}</td>
        </tr>
      </tbody>
      <tfoot v-else>
        <h6 class="p-4">No records found !!!</h6>
      </tfoot>
    </table>
    <nav class="table-responsive mb-2">
      <ul class="pagination">
        <li class="page-item"><a class="btn">Pages : </a></li>
        <li class="page-item mx-1"><a class="page-link" v-if="currentPage != 1" @click="prevPage">Previous</a></li>
        <span v-for="index in tabUpperBound" :key="index">
          <li class="page-item mx-1" v-if="index >= tabLowerBound">
            <a style="cursor: pointer;" class="page-link text-dark" :class="[currentPage == index ? 'bg-warning' : '']" @click="()=>setCurrentPage(index)">{{ index }}</a>
          </li>
        </span>
        <li v-if="currentPage != tabs && tabs != 1" class="page-item mx-1"><a class="page-link" @click="nextPage">Next</a></li>
      </ul>
    </nav>
  </div>
</template>

<script>
export default {
  name: "Body",
  data() {
    return {
      currentPage: 1,
      tabs: 10,
      tabUpperBound: 1,
      tabLowerBound: 1
    };
  },
  props: {
    equities: Array,
  },
  methods: {
    setCurrentPage(page){
      this.currentPage = page;
    },
    nextPage(){
      this.currentPage = this.currentPage + 1
    },
    prevPage(){
      this.currentPage = this.currentPage - 1
    }
  },
  watch: {
    equities(value){
      const tabs = (parseInt(value.length/20) + 1) || 1
      this.tabs = tabs
      this.tabLowerBound = 1;
      this.tabUpperBound = tabs > 10 ? 10 : tabs;
      this.currentPage = 1;
    },
    currentPage(value) {
      if(value == this.tabUpperBound && this.tabUpperBound != this.tabs){
        this.tabLowerBound = this.tabUpperBound - 1
        this.tabUpperBound = this.tabUpperBound + 10 > this.tabs ? this.tabs : this.tabUpperBound + 10;
      }
      else if(value == this.tabLowerBound && this.tabLowerBound != 1){
        this.tabUpperBound = this.tabLowerBound + 1;
        this.tabLowerBound = this.tabLowerBound - 10 < 1 ? 1 : this.tabLowerBound - 10;
      }
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
