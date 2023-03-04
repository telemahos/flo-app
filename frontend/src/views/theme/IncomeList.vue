<template>
  <div>
    <CRow>
      <CCol :md="12">
        <!-- <h2>Projects</h2> -->
        <CLink href="#/theme/incomenew"
          ><h5><CBadge color="info">Νέο Έσοδα+</CBadge></h5></CLink
        >
        <!-- <br /><br /><br /> -->
      </CCol>
    </CRow>
  </div>

  <h3>KOSTAS {{ calcoulateIncome }}</h3>

  <div>
    <CRow>
      <CCol :md="12">
        <CCard class="mb-4">
          <CCardBody>
            <CRow>
              <CCol :sm="5">
                <h4 id="traffic" class="card-title mb-0">Έσοδα</h4>
                <!-- <div class="small text-medium-emphasis">October 2022</div> -->
              </CCol>
              <CTable align="middle" class="mb-0 border" hover responsive>
                <CTableHead color="light">
                  <CTableRow>
                    <CTableHeaderCell class="text-center">
                      Hμερ.
                    </CTableHeaderCell>
                    <CTableHeaderCell>Ζ</CTableHeaderCell>
                    <CTableHeaderCell>POS</CTableHeaderCell>
                    <CTableHeaderCell class="text-center">
                      Πρ. Βάρδια
                    </CTableHeaderCell>
                    <CTableHeaderCell class="text-center"
                      >Απογ. Βάρδια</CTableHeaderCell
                    >

                    <CTableHeaderCell class="text-center"
                      >Έξοδα</CTableHeaderCell
                    >
                    <CTableHeaderCell class="text-center">
                      Υπόλοιπο
                    </CTableHeaderCell>
                    <CTableHeaderCell class="text-center">
                      Σύνολο
                    </CTableHeaderCell>
                  </CTableRow>
                </CTableHead>
                <CTableBody>
                  <CTableRow
                    v-for="income in incomes"
                    v-bind:value="income.id"
                    v-bind:key="income.date"
                  >
                    <CTableDataCell class="text-center">
                      <div>{{ income.date }}</div>
                    </CTableDataCell>
                    <CTableDataCell>
                      <div>
                        <CLink :href="link_to + income.id">{{
                          income.service_income_1 + income.bar_income_1
                        }}</CLink>
                      </div>
                      <div
                        class="small text-medium-emphasis text-truncate"
                        style="max-width: 250px"
                      >
                        {{ income.description }}
                      </div>
                    </CTableDataCell>
                    <CTableDataCell class="text-center">
                      <div>{{ income.due_date }}</div>
                    </CTableDataCell>
                    <CTableDataCell class="text-center">
                      <div class="small text-medium-emphasis">
                        <CBadge color="success">New</CBadge>
                      </div>
                    </CTableDataCell>
                    <CTableDataCell>
                      <div
                        class="small text-secondary"
                        color="text-secondary"
                        v-if="income.priority === 1"
                      >
                        Normal
                      </div>
                      <div
                        class="small text-info"
                        color="text-info"
                        v-if="income.priority === 2"
                      >
                        Medium
                      </div>
                      <div
                        class="small text-warning"
                        color="text-warning"
                        v-if="income.priority === 3"
                      >
                        High
                      </div>
                      <div
                        class="small text-danger"
                        color="text-danger"
                        v-if="income.priority === 4"
                      >
                        Critical
                      </div>
                    </CTableDataCell>
                    <CTableDataCell class="text-center">
                      <div>
                        <!-- <AppOffcanvasTicketEdit v-bind:the_case="income" /> -->
                        <CButton color="dark" variant="ghost" size="sm"
                          >Edit</CButton
                        >
                      </div>
                    </CTableDataCell>
                  </CTableRow>
                  <CTableRow> </CTableRow>

                  <!-- Total Monthly Income -->
                  <tr>
                    <td title="ΣΥΝΟΛΟ">ΣΥΝ.</td>
                    <td>
                      {{ greekMonthName[selectByMonth] }} / {{ selectByYear }}
                    </td>
                    <td>{{ totalMorningIncome }} <b>€</b></td>
                    <!-- Πρ. έσοδα -->
                    <td>{{ totalLateIncome }} <b>€</b></td>
                    <!-- Βρ. έσοδα -->
                    <td>{{ totalMonthlyIncome }} <b>€</b></td>
                    <!-- Σύνολο -->
                    <td>[11.123] €</td>
                    <!-- Έξοδα -->
                    <td>[3.123] €</td>
                    <!-- Υπόλοιπο -->
                    <td>-</td>
                    <td>[235] €</td>
                    <!-- Φ.Π.Α. -->
                    <td>-</td>
                    <td>-</td>
                    <td>-</td>
                  </tr>
                  <!-- Monthly Average -->
                  <tr>
                    <td title="ΜΕΣΟΣ ΟΡΟΣ">Μ.Ο.</td>
                    <td>{{ averageDays }}</td>
                    <td>{{ averageMorningIncome }} €</td>
                    <!-- Πρ. έσοδα -->
                    <td>{{ averageLateIncome }} €</td>
                    <!-- Βρ. έσοδα -->
                    <td>{{ averageDaylyincome }} €</td>
                    <!-- Σύνολο -->
                    <td>308 €</td>
                    <!-- Έξοδα -->
                    <td>93 €</td>
                    <!-- Υπόλοιπο -->
                    <td>-</td>
                    <td>23 €</td>
                    <!-- Φ.Π.Α. -->
                    <td>-</td>
                    <td>-</td>
                    <td>-</td>
                  </tr>
                  <tr
                    v-for="(item, index) in this.allIncomes"
                    v-bind:key="index"
                  >
                    <td>
                      <button
                        type="button"
                        class="btn btn-outline-light btn-sm"
                        @click="
                          ;(showIncomeModalEdit = true),
                            getCurrentIncome(item.id)
                        "
                      >
                        {{ item.id }}
                      </button>
                      <!-- <button @click="showIncomeModalEdit = true, getCurrentIncome(item.id)">
          <svg id="i-edit" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="20" height="20" fill="none" stroke="currentcolor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2">
              <path d="M30 7 L25 2 5 22 3 29 10 27 Z M21 6 L26 11 Z M5 22 L10 27 Z" />
          </svg>
        </button> {{item.date}} setSlotDate(item.date) -->
                    </td>
                    <td>
                      <p>{{ moment(item.date).format('dd,DD/MM/YY') }}</p>
                      <!-- <button @click="showIncomeModalEdit = true;">{{ item.date }}</button> -->
                    </td>
                    <td>
                      <p>{{ morningIncome[index] }}</p>
                    </td>
                    <td>
                      <p>{{ lateIncome[index] }}</p>
                    </td>
                    <td>
                      <p class="totalIncome">
                        <b>{{ totalDaylyIncome[index] }} </b>
                      </p>
                    </td>
                    <!--  colspan="2" -->
                    <td>
                      <p class="outcome">125 <b></b></p>
                    </td>
                    <td>
                      <p class="income"><b>329 €</b></p>
                    </td>
                    <td>{{ item.z_count }} <b>€</b></td>
                    <td>{{ item.vat }} <b>€</b></td>
                    <td>{{ item.pos }} <b>€</b></td>
                    <td :title="item.notes">
                      <div class="scrollable">
                        {{ item.notes }}
                      </div>
                    </td>
                    <td>
                      <button
                        type="button"
                        class="btn btn-outline-light btn-sm"
                        @click="deleteIncome(item.id)"
                      >
                        Χ
                        <!-- <svg id="i-trash" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="20" height="20" fill="none" stroke="currentcolor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2">
              <path d="M28 6 L6 6 8 30 24 30 26 6 4 6 M16 12 L16 24 M21 12 L20 24 M11 12 L12 24 M12 6 L13 2 19 2 20 6" />
          </svg> -->
                      </button>
                    </td>
                  </tr>
                </CTableBody>
              </CTable>
            </CRow>
          </CCardBody>
        </CCard>
      </CCol>
    </CRow>
  </div>
</template>

<script>
// import provide from 'vue'
import axios from 'axios'
import moment from 'moment'
// import AppOffcanvasTicketEdit from '../../components/AppOffcanvasTicketEdit.vue'

export default {
  name: 'IncomeList',
  components: {
    // ModalOutcome,
    // ModalIncome,
    // ModalIncomeEdit,
    // VueTailwindPagination,
  },
  data() {
    return {
      // Income Details
      id: '',
      date: '',
      shift: '',
      serviceIncome: '',
      barIncome: '',
      pos: '',
      zCount: '',
      vat: '',
      waitress: '',
      barman: '',
      notes: '',
      shift_id: '',
      // Misc
      showIncomeModal: false,
      showOutcomeModal: false,
      showIncomeModalEdit: false,
      currentDate: '',
      title: 'Επεξεργασία Εσόδων',
      token: this.$store.state.token,
      today: this.$store.state.today,
      year: '',
      month: '',
      day: '',
      list: '',
      singleIncome: '',
      staff: '',
      shiftStaff: '',
      sum: '',
      apiURL: this.$store.state.apiURL,
      currentShift: '',
      waitressSelect: [],
      barmanSelect: [],
      staffLength: 0,
      allIncomes: [],
      // tailwind pagination
      currentPage: 1,
      perPage: 15,
      total: 0,
      // Calculations Dayly
      morningIncome: [],
      lateIncome: [],
      totalDaylyIncome: [],
      totalDaylyOutcome: 0,
      totalDaylyRest: 0,
      // Calculations Monthly
      totalMorningIncome: 0,
      totalLateIncome: 0,
      totalMonthlyIncome: 0,
      // Average Calculations
      averageDays: 0,
      averageMorningIncome: 0,
      averageLateIncome: 0,
      averageDaylyincome: 0,
      // Select Income by Month and Year
      selectByMonth: '',
      selectByYear: '',
      dayjs: '',
      greekMonthName: [
        '0',
        'ΙΑΝ',
        'ΦΕΒ',
        'ΜΑΡ',
        'ΑΠΡ',
        'ΜΑΙ',
        'ΙΟΥΝ',
        'ΙΟΥΛ',
        'ΑΥΓ',
        'ΣΕΠ',
        'ΟΚΤ',
        'ΝΟΕ',
        'ΔΕΚ',
      ],
    }
  },
  created: function () {
    this.moment = moment
    moment.locale('el')
    // this.year = this.today.getFullYear()
    this.year = '2021'
    // this.day = this.today.getDate()
    this.day = '09'
    // this.month = this.today.getMonth() + 1
    this.month = '05'
    // To be the Year and Month selected at the page Loading
    this.selectByMonth = this.month
    this.selectByYear = this.year
    console.log('THIS YEAR: ' + this.year)
    console.log('THIS selectByYear: ' + this.selectByYear)
  },
  // BeforeMounted
  // ###########################################################
  beforeMount() {
    this.getAllIncomes()
  },
  // Mounted
  // ###########################################################
  mounted() {
    
    
    // this.calcoulateIncome()
    // this.getAllOutcomes()
    console.log('TODAY IS THE MONTH: ', this.month)
    
    // console.log("this.calcoulateIncome: ", this.averageDaylyincome)
  },
  // computed ###########################################################
  computed: {
    // calcoulateIncome() {
    //   return this.totalMonthlyIncome
    // },
  }, // computed

  beforeUpdate() {
    // Reset total Incomes before updating anything
    this.totalMorningIncome = 0
    this.totalLateIncome = 0
    this.totalMonthlyIncome = 0
  },

  // Methods
  // ###########################################################
  methods: {
    // BeforeMounted
    calcoulateIncome() {
      console.log('CALCOULATE INCOME 73!!')
      // console.log('this.allIncome: ', this.allIncomes)
      for (let i = 0; i < this.allIncomes.length; i++) {
        // console.log('allIncome[i]#####: ' + this.allIncomes[i].id)
        console.log('this.allIncomes[i]: ' + '737373')

        this.morningIncome[i] = parseFloat(
          this.allIncomes[i].service_income_1 + this.allIncomes[i].bar_income_1,
        ).toFixed(2)
        this.totalMorningIncome += Math.round(this.morningIncome[i])
        console.log('this.totalMorningIncome: ' + this.totalMorningIncome)
        this.lateIncome[i] = parseFloat(
          this.allIncomes[i].service_income_2 + this.allIncomes[i].bar_income_2,
        ).toFixed(2)
        this.totalLateIncome += Math.round(this.lateIncome[i])
        console.log('this.totalLateIncome ' + this.totalLateIncome)
        this.totalDaylyIncome[i] =
          parseFloat(this.morningIncome[i]) + parseFloat(this.lateIncome[i])
        this.totalDaylyIncome[i] = this.totalDaylyIncome[i].toFixed(2)
        this.totalMonthlyIncome += Math.round(this.totalDaylyIncome[i])
        console.log('this.totalMonthlyIncome[i]: ' + this.totalMonthlyIncome)
      }
      this.averageDays = this.allIncomes.length
      this.averageMorningIncome = Math.round(
        this.totalMorningIncome / this.averageDays,
      )
      this.averageLateIncome = Math.round(
        this.totalLateIncome / this.averageDays,
      )
      this.averageDaylyincome = Math.round(
        this.totalMonthlyIncome / this.averageDays,
      )
      console.log('this.averageMorningIncome: ' + this.averageDaylyincome)
      return this.averageDaylyincome
    },
    // Get All INCOME from DB
    async getAllIncomes() {
      // console.log('apiURL2: ', this.apiURL)
      await axios
        .get(
          `${this.$store.state.apiURL}/income/${this.year}/${this.month}` +
            `?page=` +
            this.currentPage +
            `&size=` +
            this.perPage,
          {
            headers: {
              Authorization: `Bearer ${this.token}`,
              'Content-Type': 'application/json',
            },
          },
        )
        .then((response) => {
          // console.log('list Income: ' + JSON.stringify(response.data))
          // handle success
          this.allIncomes = response.data
          console.log('this.allIncomes: ' + this.allIncomes)
          this.currentPage = response.data.page
          // console.log('this.allIncomes: ' + JSON.stringify(this.currentPage))
          this.perPage = response.data.size
          this.total = response.data.total
          
        })
        .catch((error) => console.log(error))
        // Calculate Sums of morning, evening and total Income of the Day
        .finally(() => {})

      //  Get all staff from DB
      const headers = {
        Authorization: `Bearer ${this.token}`,
        'Content-Type': 'application/json',
        // 'Content-Type': 'application/x-www-form-urlencoded',
      }
      await axios
        .get(`${this.apiURL}/staff`, { headers })
        .then((response) => {
          this.staff = response.data
          // console.log('Staff', this.staff)
        })
        .finally(() => {
          // Εδώ αποθηκεύονται οι Μπαρμαν και οι Σερβιτόρες για το Select
          // waitressSelect: [] και barmanSelect: []
          this.staffLength = this.staff.length
          // console.log("staffLength: " + this.staffLength)
          let y = 0,
            z = 0

          for (let i = 0; i < this.staffLength; i++) {
            console.log('i: ' + JSON.stringify(this.staff[i].position))
            // waitressSelect
            if (this.staff[i].position === 'Service') {
              this.waitressSelect[y] = this.staff[i]
              // console.log('waitressSelect: ' + this.waitressSelect[y].name)
              y++
            } else if (this.staff[i].position === 'Barman') {
              this.barmanSelect[z] = this.staff[i]
              // console.log('barmanSelect: ' + this.barmanSelect[z].name)
              z++
            }
          }
        })
        .catch((error) => console.log(`${error}`))
    },

    // Get All OUTCOME from DB
    async getAllOutcomes() {
      console.log('OUTCOME')
      await axios
        .get(
          `${this.$store.state.apiURL}/outcome/${this.year}/${this.month}` +
            `?page=` +
            this.currentPage +
            `&size=` +
            this.perPage,
          {
            headers: {
              Authorization: `Bearer ${this.token}`,
              'Content-Type': 'application/json',
            },
          },
        )
        .then((response) => {
          // console.log('list Income: ' + JSON.stringify(response.data))
          // handle success
          this.allOutcomes = response.data.items
          // this.currentPage = response.data.page
          // this.perPage = response.data.size
          // this.total = response.data.total
          // console.log('this.allOUTcomes: ' + JSON.stringify(response.data))
        })
        .catch((error) => console.log(error))
        // Calculate Sums of morning, evening and total Income of the Day
        .finally(() => {})
    },

    showIncomeByMonth() {
      this.month = this.selectByMonth
      this.year = this.selectByYear
      // console.log("GO")
      // console.log('selectByMonth; ' + this.selectByMonth)
      // console.log('selectByYear: ' + this.selectByYear)
      // Add first char in Month by zero if month is between 1-9
      if (parseInt(this.month) <= 9) {
        // console.log('MONTH HAS ONE DIGIT22: 0', this.month)
        this.month = '0' + this.month
        // console.log("CONCAT MONTH: ", this.month)
      }
      // Call getAllIncomes() to get next data
      this.getAllIncomes()
      this.getAllOutcomes()
    },

    percentage(key1, key2) {
      let total = key1 + key2
      return total * 100
    },

    // Format the date
    setSlotDate(theDate) {
      // dayjs.locale('gr')
      // this.currentDate = dayjs(theDate)
      console.log('theDate: ' + theDate)
      return this.currentDate.format('dd,DD.MM.YY')
    },

    getCurrentIncome(id) {
      console.log('getCurrentIncome MeTHODo:: ' + id)
      axios
        .get(`${this.$store.state.apiURL}/income/` + id, {
          headers: {
            Authorization: `Bearer ${this.token}`,
          },
        })
        .then((response) => {
          console.log('singleIncome: ' + response.data)
          // handle success
          this.singleIncome = response.data
          this.shiftStaff = this.singleIncome.the_shift
        })
        .catch((error) => console.log(error))
        .finally(() => {
          console.log('singleIncome.shift_id' + this.singleIncome.shift_id)
          this.getCurrentShift(this.singleIncome.shift_id)
        })
    },

    getCurrentShift(id) {
      console.log('getCurrentShift ID:: ' + id)
      axios
        .get(`${this.$store.state.apiURL}/shift/` + id, {
          headers: {
            Authorization: `Bearer ${this.token}`,
          },
        })
        .then((response) => {
          console.log('currentShift' + response.data)
          // handle success
          this.currentShift = response.data
        })
        .catch((error) => console.log(error))
        .finally(() => {
          console.log('currentShift' + JSON.stringify(this.currentShift))
        })
    },

    deleteIncome(id) {
      console.log('Delete Income ID:: ' + id)
      axios
        .delete(`${this.$store.state.apiURL}/income/` + id, {
          headers: {
            Authorization: `Bearer ${this.token}`,
          },
        })
        .then((response) => {
          console.log('DELETED: ' + response)
          // handle success
          this.currentShift = response.data
        })
        .catch((error) => console.log(error))
        .finally(() => {
          this.getAllIncomes()
        })
    },

    // Pagination
    onPageClick(event) {
      this.currentPage = event
      // console.log("CLICK!!!");
      this.getAllIncomes()
    },
  }, // methods
}
</script>
