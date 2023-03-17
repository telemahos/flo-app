<template>
  <div>
    <CRow>
      <CCol :md="2">
        <CLink href="#/theme/incomenew"
          ><h5><CBadge color="info">Νέο Έσοδα+</CBadge></h5></CLink
        >
      </CCol>
    </CRow>
  </div>

  {{ calcoulateIncome }}
  <!-- Total Monthly Income -->
  <h3>ΣΥΝΟΛΟ ΜΗΝΑ: {{ greekMonthName[selectByMonth] }} / {{ selectByYear }} - ΗΜΕΡΕΣ: {{ averageDays }}</h3>
  <!-- <CWidgetIncome /> -->

  <CRow>
    <CCol :xs="3">
      <CWidgetStatsB class="mb-3" :progress="{ color: 'secondary', value: 100 }">
        <template #text>Μ.Ο. {{ formatPrice(averageMorningIncome) }}</template>
        <template #title>ΠΡΩΤΗ ΒΑΡΔΙΑ</template>
        <template #value>
          {{ formatPrice(dailyTotalMorningIncome) }}
        </template>
      </CWidgetStatsB>
    </CCol>
    <CCol :xs="3">
      <CWidgetStatsB class="mb-3" :progress="{ color: 'info', value: 100 }">
        <template #text>Μ.Ο. {{ formatPrice(averageLateIncome) }}</template>
        <template #title>ΔΕΥΤΕΡΗ ΒΑΡΔΙΑ</template>
        <template #value>
          {{ formatPrice(dailyTotalLateIncome) }}
        </template>
      </CWidgetStatsB>
    </CCol>
    <CCol :xs="3">
      <CWidgetStatsB class="mb-3" :progress="{ color: 'danger', value: 100 }">
        <template #text>Widget helper text</template>
        <template #title>ΕΞΟΔΑ ΜΗΝΑ</template>
        <template #value>$98.111,00</template>
      </CWidgetStatsB>
    </CCol>
    <CCol :xs="3">
      <CWidgetStatsB
        class="mb-3"
        :progress="{ color: 'success', value: 100}"
        >
        <template #text>Μ.Ο. {{ formatPrice(averageDaylyincome) }}</template>
        <template #title>ΕΣΟΔΑ ΜΗΝΑ</template>
        <template #value>{{ formatPrice(totalMonthlyIncome) }}</template>
      </CWidgetStatsB>
    </CCol>
  </CRow>

  <div>
    <CRow>
      <CCol :md="12">
        <CCard class="mb-4">
          <CCardBody>
            <CRow>
              <CCol :sm="5">
                <h4 id="traffic" class="card-title mb-0">ΜΗΝΑΣ</h4>
                <!-- <div class="small text-medium-emphasis">October 2022</div> -->
              </CCol>
              <CTable align="middle" class="mb-0 border" hover responsive>
                <CTableHead color="light">
                  <CTableRow>
                    <CTableHeaderCell class="text-center">
                      A/A
                    </CTableHeaderCell>
                    <CTableHeaderCell class="text-center">
                      Hμερ.
                    </CTableHeaderCell>
                    <CTableHeaderCell class="text-center">
                      Πρωί
                    </CTableHeaderCell>
                    <CTableHeaderCell class="text-center"
                      >Απογ.</CTableHeaderCell
                    >
                    <CTableHeaderCell class="text-center">
                      Σύνολο
                    </CTableHeaderCell>
                    <CTableHeaderCell class="text-center"
                      >Έξοδα</CTableHeaderCell
                    >
                    <CTableHeaderCell class="text-center">
                      Υπόλοιπο
                    </CTableHeaderCell>
                    <CTableHeaderCell>Ζ</CTableHeaderCell>
                    <CTableHeaderCell>Φ.Π.Α.</CTableHeaderCell>
                    <!-- <CTableHeaderCell>POS</CTableHeaderCell> -->
                    <CTableHeaderCell>Σημείωση</CTableHeaderCell>
                    <CTableHeaderCell>Επεξ.</CTableHeaderCell>
                  </CTableRow>
                </CTableHead>
                <CTableBody>
                  <!--<CTableRow
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
                     < ! -- <div
                        class="small text-medium-emphasis text-truncate"
                        style="max-width: 250px"
                      >
                        {{ income.description }}
                      </div> -- >
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
                        < ! -- <AppOffcanvasTicketEdit v-bind:the_case="income" /> -- >
                        <CButton color="dark" variant="ghost" size="sm"
                          >Edit</CButton
                        >
                      </div>
                    </CTableDataCell>
                  </CTableRow> -->
                  <CTableRow> </CTableRow>
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
                    </td>
                    <td class="small">
                      {{ moment(item.date).format('dd DD') }}
                    </td>
                    <td>
                      {{ formatPrice(dailyMorningIncome[index]) }}
                    </td>
                    <td>
                      {{ formatPrice(dailyLateIncome[index]) }}
                    </td>
                    <td>
                      <div class="dailyTotalIncome">
                        {{ formatPrice(totalDaylyIncome[index]) }}
                      </div>
                    </td>
                    <td>
                      <div
                        v-if="!isNaN(dictTotalDailyOutcome[item.date])"
                        class="dailyTotalOutcome"
                      >
                        {{ formatPrice(dictTotalDailyOutcome[item.date]) }}
                      </div>
                      <div class="dailyTotalOutcome" v-else>
                        {{ formatPrice(0) }}
                      </div>
                    </td>
                    <td>
                      <div class="income">
                        {{
                          formatPrice(
                            totalDaylyIncome[index] -
                              dictTotalDailyOutcome[item.date],
                          )
                        }}
                      </div>
                    </td>
                    <td>{{ formatPrice(item.z_count) }}</td>
                    <td>{{ formatPrice(item.vat) }}</td>
                    <!-- <td>{{ item.pos }} <b>€</b></td> -->
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
// import CWidgetIncome from '../widgets/WidgetIncome.vue'
// import AppOffcanvasTicketEdit from '../../components/AppOffcanvasTicketEdit.vue'

export default {
  name: 'IncomeList',
  components: {
    // CWidgetIncome,
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
      // Calculations Dayly Income
      dailyMorningIncome: [],
      dailyLateIncome: [],
      totalDaylyIncome: [],
      totalDaylyOutcome: 0,
      totalDaylyRest: 0,
      // Calculations Monthly
      dailyTotalMorningIncome: 0,
      dailyTotalLateIncome: 0,
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
      // Outcome
      monthlyOutcomeLength: '',
      allOutcomes: '',
      totalDailyOutcome: '',
      dictTotalDailyOutcome: {},
      // Income
      // dictTotalDailyIncome: {},
      // Months
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
    this.getAllOutcomes()
    this.getAllIncomes()
  },
  // Mounted
  // ###########################################################
  mounted() {
    // this.getAllOutcomes()
    console.log('TODAY IS THE MONTH: ', this.month)

    // console.log("this.calcoulateIncome: ", this.averageDaylyincome)
  },
  // computed ###########################################################
  computed: {
    calcoulateIncome() {
      this.averageDays = this.allIncomes.length
      // console.log('CALCOULATE INCOME 73!!')
      for (let i = 0; i < this.allIncomes.length; i++) {
        // console.log('allIncome[i]#####: ' + this.allIncomes[i].id)
        this.dailyMorningIncome[i] = parseFloat(
          this.allIncomes[i].service_income_1 + this.allIncomes[i].bar_income_1,
        ).toFixed(2)
        this.dailyTotalMorningIncome += Math.round(this.dailyMorningIncome[i])
        // console.log('this.dailyTotalMorningIncome: ' + this.dailyTotalMorningIncome)
        this.dailyLateIncome[i] = parseFloat(
          this.allIncomes[i].service_income_2 + this.allIncomes[i].bar_income_2,
        ).toFixed(2)
        this.dailyTotalLateIncome += Math.round(this.dailyLateIncome[i])
        // console.log('this.dailyTotalLateIncome ' + this.dailyTotalLateIncome)
        this.totalDaylyIncome[i] =
          parseFloat(this.dailyMorningIncome[i]) +
          parseFloat(this.dailyLateIncome[i])
        // this.totalDaylyIncome[i] = this.totalDaylyIncome[i].toFixed(2)
        this.totalMonthlyIncome += Math.round(this.totalDaylyIncome[i])
        // console.log('this.totalMonthlyIncome[i]: ' + this.totalMonthlyIncome)

        // Avarage, to be contineud
        this.averageMorningIncome = Math.round(
          // this.dailyTotalMorningIncome / this.averageDays,
          this.dailyTotalMorningIncome / [i + 1],
        )
        // console.log('this.averageDays: ', this.averageDays)
        // console.log('this.averageMorningIncome: ' + this.averageMorningIncome)
        this.averageLateIncome = Math.round(
          // this.dailyTotalLateIncome / this.averageDays,
          this.dailyTotalLateIncome / [i + 1],
        )
        this.averageDaylyincome = Math.round(
          // this.totalMonthlyIncome / this.averageDays,
          this.totalMonthlyIncome / [i + 1],
        )
      }

      // console.log('this.averageMorningIncome: ' + this.averageDaylyincome)
      return this.averageDaylyincome
    },
  }, // computed

  beforeUpdate() {
    // Reset total Incomes before updating anything
    this.dailyTotalMorningIncome = 0
    this.dailyTotalLateIncome = 0
    this.totalMonthlyIncome = 0
  },

  // Methods
  // ###########################################################
  methods: {
    // Currency Formater
    formatPrice(value) {
      let val = (value / 1).toFixed(2).replace('.', ',')
      return val.toString().replace(/\B(?=(\d{3})+(?!\d))/g, '.') + '€'
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
          // console.log('this.allIncomes: ' + this.allIncomes)
          // this.currentPage = response.data.page
          // console.log('this.allIncomes: ' + JSON.stringify(this.currentPage))
          // this.perPage = response.data.size
          // this.total = response.data.total
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
          this.allOutcomes = response.data
          this.monthlyOutcomeLength = this.allOutcomes.length
          console.log('monthlyOutcomeLength: ', this.monthlyOutcomeLength)
          // add to a Dictionary all daily expenses as a sum (dictTotalDailyOutcome)
          if (this.monthlyOutcomeLength > 0) {
            for (let i = 0; i < this.monthlyOutcomeLength; i++) {
              if (this.allOutcomes[i].date in this.dictTotalDailyOutcome) {
                this.dictTotalDailyOutcome[this.allOutcomes[i].date] +=
                  this.allOutcomes[i].cost
              } else {
                this.dictTotalDailyOutcome[this.allOutcomes[i].date] =
                  this.allOutcomes[i].cost
              }
              console.log('INCOMEDATE2: ', this.allOutcomes[i].date)
              console.log(
                'TOTAL DAILY OUTCOME: ',
                this.dictTotalDailyOutcome[this.allOutcomes[i].date],
              )
              console.log('-------------------', [i])
            }
          }

          //
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
      this.getAllOutcomes()
      this.getAllIncomes()
    },

    percentage(key1, key2) {
      let total = key1 + key2
      return total * 100
    },

    // Format the date
    setSlotDate(theDate) {
      // dayjs.locale('gr')
      // this.currentDate = dayjs(theDate)
      // console.log('theDate: ' + theDate)
      return this.currentDate.format('dd,DD.MM.YY')
    },

    getCurrentIncome(id) {
      // console.log('getCurrentIncome MeTHODo:: ' + id)
      axios
        .get(`${this.$store.state.apiURL}/income/` + id, {
          headers: {
            Authorization: `Bearer ${this.token}`,
          },
        })
        .then((response) => {
          // console.log('singleIncome: ' + response.data)
          // handle success
          this.singleIncome = response.data
          this.shiftStaff = this.singleIncome.the_shift
        })
        .catch((error) => console.log(error))
        .finally(() => {
          // console.log('singleIncome.shift_id' + this.singleIncome.shift_id)
          this.getCurrentShift(this.singleIncome.shift_id)
        })
    },

    getCurrentShift(id) {
      // console.log('getCurrentShift ID:: ' + id)
      axios
        .get(`${this.$store.state.apiURL}/shift/` + id, {
          headers: {
            Authorization: `Bearer ${this.token}`,
          },
        })
        .then((response) => {
          // console.log('currentShift' + response.data)
          // handle success
          this.currentShift = response.data
        })
        .catch((error) => console.log(error))
        .finally(() => {
          // console.log('currentShift' + JSON.stringify(this.currentShift))
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

<style>
.dailyTotalIncome {
  color: yellowgreen;
}
.dailyTotalOutcome {
  color: tomato;
}
.table > :not(caption) > * > * {
  font-size: 14px;
}
td.small {
  font-size: 9px;
}
</style>
