<template>

  <div class="row g-3 justify-content-center"> 
      
    <div class="col-md-2">
      <label class="visually-hidden" for="selectByMonth">SelectByMonth</label>
      <select class="form-select form-select-sm" aria-label="Default select example" id="selectByMonth" name="selectByMonth" v-model="selectByMonth">
        <!-- <option disabled value>Σερβ1...</option> -->
        <option :selected="month === 1" value="1">Ιανουάριος</option>
        <option :selected="month === 2" value="2">Φεβρουάριος</option>
        <option :selected="month === 3" value="3">Μάρτιος</option>
        <option :selected="month === 4" value="4">Απρίλιος</option>
        <option :selected="month === 5" value="5">Μάιος</option>
        <option :selected="month === 6" value="6">Ιούνιος</option>
        <option :selected="month === 7" value="7">Ιούλιος</option>
        <option :selected="month === 8" value="8">Αύγουστος</option>
        <option :selected="month === 9" value="9">Σεπτέμβριος</option>
        <option :selected="month === 10" value="10">Οκτώβριος</option>
        <option :selected="month === 11" value="11">Νοέμβριος</option>
        <option :selected="month === 12" value="12">Δεκέμβριος</option>
      </select>
    </div>

    <div class="col-md-1">
      <label class="visually-hidden" for="selectByMonth">SelectByMonth</label>
      <!-- Year -->
      <select class="form-select form-select-sm" aria-label="Default select example" id="selectByYear" name="selectByYear" v-model="selectByYear">
        <!-- <option disabled value>Σερβ1...</option> -->
        <option :selected="year === 2021" value="2021">2021</option>
        <option :selected="year === 2022" value="2022">2022</option>
        <option :selected="year === 2023" value="2023">2023</option>
        <option :selected="year === 2024" value="2024">2024</option>
        <option :selected="year === 2025" value="2025">2025</option>
        <option :selected="year === 2026" value="2026">2026</option>
      </select>
    </div>

    <div class="col-md-1">
      <label class="visually-hidden" for="perPage">perPage</label>
      <!-- Year -->
      <select class="form-select form-select-sm" aria-label="Default select example" id="perPage" name="perPage" v-model="perPage">
        <!-- <option disabled value>Σερβ1...</option> -->
        <option :selected="perPage === 5" value="5">5</option>
        <option :selected="perPage === 10" value="10">10</option>
        <option :selected="perPage === 15" value="15">15</option>
        <option :selected="perPage === 20" value="20">20</option>
        <option :selected="perPage === 31" value="31">ΟΛΑ</option>
      </select>
    </div>

    <!-- Btn OutCome -->
    <div class="col-md-1">
      <button class="btn btn-primary" @click="showIncomeByMonth()" type="submit">GO</button>
    </div>
  </div>

</template>