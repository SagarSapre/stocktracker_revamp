'use strict';

var favReport = void 0,
    derivativeFavReport = void 0,
    debtFavReport = void 0;
B.on(document, 'allGood', function () {
    var marketResults = {};
    var reportType = getParameterByName('type');
    if (reportType) {
        switch (reportType) {
            case "capital":
                $('#capitalMarket').trigger('click');
                break;
            case "derivative":
                $('#derivativeMarket').trigger('click');
                break;
            case "debt":
                $('#debtMarket').trigger('click');
                break;
        }
    }
    var getNextTradingDate = function getNextTradingDate(data) {
        return data ? data.marketNextTradingDate || data.tradeDate || '-' : "-";
    };
    var getCurrentTradingDate = function getCurrentTradingDate(data) {
        return data ? data.marketCurrentTradingDate || data.tradeDate || '-' : "-";
    };
    var getAllMarketStatus = function getAllMarketStatus() {
        return new Promise(function (resolve, reject) {
            B.get('/api/allMarketStatus').then(function (res) {
                var data = [];
                if (res) {
                    data = JSON.parse(res);
                    data.forEach(function (d) {
                        if (d) {
                            marketResults[d.market] = d;
                        }
                    });
                    var symbol = ["CM", "INDEX", "SLBS", "SME", "FO", "COM", "CD", "NBF", "WDM", "CBM", "TRI-PARTY"];
                    symbol.forEach(function (name) {
                        B.get('/api/daily-reports?key=' + name).then(function (resp) {
                            var respJSON = [];
                            if (resp !== "") {
                                respJSON = JSON.parse(resp);
                            }
                            var dailyReports = void 0,
                                dailyReportsPrev = void 0,
                                dailyReportsFuture = void 0;
                            switch (name) {
                                case "CM":
                                    $('#cr_equity_currentDate').text(respJSON.currentDate || "-");
                                    $('#cr_equity_prevDate').text(respJSON.previousDate || "-");
                                    $('#cr_equity_futureDate').text(getNextTradingDate(marketResults["CM"]));

                                    dailyReportsFuture = ReportCard({ cardStyle: { class: 'row col-12' }, data: respJSON.FutureDay || [], info: { name: "capital-market", section: "equities", type: "daily-reports" } });
                                    B.render(dailyReportsFuture, B.findOne('#cr_equity_daily_Future'));

                                    dailyReports = ReportCard({ cardStyle: { class: 'row col-12' }, data: respJSON.CurrentDay || [], info: { name: "capital-market", section: "equities", type: "daily-reports" } });
                                    B.render(dailyReports, B.findOne('#cr_equity_daily_Current'));

                                    dailyReportsPrev = ReportCard({ cardStyle: { class: 'row col-12' }, data: respJSON.PreviousDay || [], info: { name: "capital-market", section: "equities", type: "daily-reports" } });
                                    B.render(dailyReportsPrev, B.findOne('#cr_equity_daily_Previous'));
                                    break;
                                case "INDEX":
                                    $('#cr_indices_currentDate').text(getCurrentTradingDate(marketResults["CM"]));
                                    $('#cr_indices_prevDate').text(respJSON.previousDate || "-");
                                    $('#cr_indices_futureDate').text(getNextTradingDate(marketResults["CM"]));

                                    dailyReportsFuture = ReportCard({ cardStyle: { class: 'row col-12' }, data: respJSON.FutureDay || [], info: { name: "capital-market", section: "indices", type: "daily-reports" } });
                                    B.render(dailyReportsFuture, B.findOne('#cr_indices_daily_Future'));

                                    dailyReports = ReportCard({ cardStyle: { class: 'row col-12' }, data: respJSON.CurrentDay || [], info: { name: "capital-market", section: "indices", type: "daily-reports" } });
                                    B.render(dailyReports, B.findOne('#cr_indices_daily_Current'));

                                    dailyReportsPrev = ReportCard({ cardStyle: { class: 'row col-12' }, data: respJSON.PreviousDay || [], info: { name: "capital-market", section: "indices", type: "daily-reports" } });
                                    B.render(dailyReportsPrev, B.findOne('#cr_indices_daily_Previous'));
                                    break;
                                case "SLBS":
                                    $('#cr_ssbs_currentDate').text(respJSON.currentDate || "-");
                                    $('#cr_ssbs_prevDate').text(respJSON.previousDate || "-");
                                    $('#cr_issbs_futureDate').text(getNextTradingDate(marketResults["CM"]));

                                    dailyReportsFuture = ReportCard({ cardStyle: { class: 'row col-12' }, data: respJSON.FutureDay || [], info: { name: "capital-market", section: "slb", type: "daily-reports" } });
                                    B.render(dailyReportsFuture, B.findOne('#cr_ssbs_daily_Future'));

                                    dailyReports = ReportCard({ cardStyle: { class: 'row col-12' }, data: respJSON.CurrentDay || [], info: { name: "capital-market", section: "slb", type: "daily-reports" } });
                                    B.render(dailyReports, B.findOne('#cr_ssbs_daily_Current'));

                                    dailyReportsPrev = ReportCard({ cardStyle: { class: 'row col-12' }, data: respJSON.PreviousDay || [], info: { name: "capital-market", section: "slb", type: "daily-reports" } });
                                    B.render(dailyReportsPrev, B.findOne('#cr_ssbs_daily_Previous'));
                                    break;
                                case "SME":
                                    $('#cr_sme_currentDate').text(respJSON.currentDate || "-");
                                    $('#cr_sme_prevDate').text(respJSON.previousDate || "-");
                                    $('#cr_sme_futureDate').text(getNextTradingDate(marketResults["CM"]));

                                    dailyReportsFuture = ReportCard({ cardStyle: { class: 'row col-12' }, data: respJSON.FutureDay || [], info: { name: "capital-market", section: "sme", type: "daily-reports" } });
                                    B.render(dailyReportsFuture, B.findOne('#cr_sme_daily_Future'));

                                    dailyReports = ReportCard({ cardStyle: { class: 'row col-12' }, data: respJSON.CurrentDay || [], info: { name: "capital-market", section: "sme", type: "daily-reports" } });
                                    B.render(dailyReports, B.findOne('#cr_sme_daily_Current'));

                                    dailyReportsPrev = ReportCard({ cardStyle: { class: 'row col-12' }, data: respJSON.PreviousDay || [], info: { name: "capital-market", section: "sme", type: "daily-reports" } });
                                    B.render(dailyReportsPrev, B.findOne('#cr_sme_daily_Previous'));
                                    break;
                                case "FO":
                                    $('#cr_deriv_equity_currentDate').text(respJSON.currentDate || "-");
                                    $('#cr_deriv_equity_prevDate').text(respJSON.previousDate || "-");
                                    $('#cr_deriv_equity_futureDate').text(getNextTradingDate(marketResults["FO"]));

                                    dailyReportsFuture = ReportCard({ cardStyle: { class: 'row col-12' }, data: respJSON.FutureDay || [], info: { name: "derivatives", section: "equity", type: "daily-reports" } });
                                    B.render(dailyReportsFuture, B.findOne('#cr_deriv_equity_daily_Future'));

                                    $('#foCumulativePerMsg').text(respJSON.foCumulativePer || '---');

                                    dailyReports = ReportCard({ cardStyle: { class: 'row col-12' }, data: respJSON.CurrentDay || [], info: { name: "derivatives", section: "equity", type: "daily-reports" } });
                                    B.render(dailyReports, B.findOne('#cr_deriv_equity_daily_Current'));

                                    dailyReportsPrev = ReportCard({ cardStyle: { class: 'row col-12' }, data: respJSON.PreviousDay || [], info: { name: "derivatives", section: "equity", type: "daily-reports" } });
                                    B.render(dailyReportsPrev, B.findOne('#cr_deriv_equity_daily_Previous'));
                                    break;
                                case "COM":
                                    $('#cr_derv_commodity_currentDate').text(respJSON.currentDate || "-");
                                    $('#cr_derv_commodity_prevDate').text(respJSON.previousDate || "-");
                                    $('#cr_derv_commodity_futureDate').text(getNextTradingDate(marketResults["COM"]));

                                    dailyReportsFuture = ReportCard({ cardStyle: { class: 'row col-12' }, data: respJSON.FutureDay || [], info: { name: "derivatives", section: "commodity", type: "daily-reports" } });
                                    B.render(dailyReportsFuture, B.findOne('#cr_derv_commodity_daily_Future'));

                                    dailyReports = ReportCard({ cardStyle: { class: 'row col-12' }, data: respJSON.CurrentDay || [], info: { name: "derivatives", section: "commodity", type: "daily-reports" } });
                                    B.render(dailyReports, B.findOne('#cr_derv_commodity_daily_Current'));

                                    dailyReportsPrev = ReportCard({ cardStyle: { class: 'row col-12' }, data: respJSON.PreviousDay || [], info: { name: "derivatives", section: "commodity", type: "daily-reports" } });
                                    B.render(dailyReportsPrev, B.findOne('#cr_derv_commodity_daily_Previous'));
                                    break;
                                case "CD":
                                    $('#cr_derv_currency_currentDate').text(respJSON.currentDate || "-");
                                    $('#cr_derv_currency_prevDate').text(respJSON.previousDate || "-");
                                    $('#cr_derv_currency_futureDate').text(getNextTradingDate(marketResults["CD"]));

                                    dailyReportsFuture = ReportCard({ cardStyle: { class: 'row col-12' }, data: respJSON.FutureDay || [], info: { name: "derivatives", section: "currency", type: "daily-reports" } });
                                    B.render(dailyReportsFuture, B.findOne('#cr_derv_currency_daily_Future'));

                                    dailyReports = ReportCard({ cardStyle: { class: 'row col-12' }, data: respJSON.CurrentDay || [], info: { name: "derivatives", section: "currency", type: "daily-reports" } });
                                    B.render(dailyReports, B.findOne('#cr_derv_currency_daily_Current'));

                                    dailyReportsPrev = ReportCard({ cardStyle: { class: 'row col-12' }, data: respJSON.PreviousDay || [], info: { name: "derivatives", section: "currency", type: "daily-reports" } });
                                    B.render(dailyReportsPrev, B.findOne('#cr_derv_currency_daily_Previous'));
                                    break;
                                case "NBF":
                                    $('#cr_derv_irf_currentDate').text(respJSON.currentDate || "-");
                                    $('#cr_derv_irf_prevDate').text(respJSON.previousDate || "-");
                                    $('#cr_derv_irf_futureDate').text(getNextTradingDate(marketResults["IRD"]));

                                    dailyReportsFuture = ReportCard({ cardStyle: { class: 'row col-12' }, data: respJSON.FutureDay || [], info: { name: "derivatives", section: "irf", type: "daily-reports" } });
                                    B.render(dailyReportsFuture, B.findOne('#cr_derv_irf_daily_Future'));

                                    dailyReports = ReportCard({ cardStyle: { class: 'row col-12' }, data: respJSON.CurrentDay || [], info: { name: "derivatives", section: "irf", type: "daily-reports" } });
                                    B.render(dailyReports, B.findOne('#cr_derv_irf_daily_Current'));

                                    dailyReportsPrev = ReportCard({ cardStyle: { class: 'row col-12' }, data: respJSON.PreviousDay || [], info: { name: "derivatives", section: "irf", type: "daily-reports" } });
                                    B.render(dailyReportsPrev, B.findOne('#cr_derv_irf_daily_Previous'));
                                    break;
                                case "WDM":
                                    $('#cr_debt_segment_currentDate').text(getCurrentTradingDate(marketResults["NTRP"]));
                                    $('#cr_debt_segment_prevDate').text(respJSON.previousDate || "-");
                                    $('#cr_debt_segment_futureDate').text(getNextTradingDate(marketResults["NTRP"]));

                                    dailyReportsFuture = ReportCard({ cardStyle: { class: 'row col-12' }, data: respJSON.FutureDay || [], info: { name: "debt", section: "debt-segment", type: "daily-reports" } });
                                    B.render(dailyReportsFuture, B.findOne('#cr_debt_segment_daily_Future'));

                                    dailyReports = ReportCard({ cardStyle: { class: 'row col-12' }, data: respJSON.CurrentDay || [], info: { name: "debt", section: "debt-segment", type: "daily-reports" } });
                                    B.render(dailyReports, B.findOne('#cr_debt_segment_daily_Current'));

                                    dailyReportsPrev = ReportCard({ cardStyle: { class: 'row col-12' }, data: respJSON.PreviousDay || [], info: { name: "debt", section: "debt-segment", type: "daily-reports" } });
                                    B.render(dailyReportsPrev, B.findOne('#cr_debt_segment_daily_Previous'));
                                    break;
                                case "CBM":
                                    $('#cr_debt_cb_currentDate').text(getCurrentTradingDate(marketResults["CBM"]));
                                    $('#cr_debt_cb_prevDate').text(respJSON.previousDate || "-");
                                    $('#cr_debt_cb_futureDate').text(getNextTradingDate(marketResults["CBM"]));

                                    dailyReportsFuture = ReportCard({ cardStyle: { class: 'row col-12' }, data: respJSON.FutureDay || [], info: { name: "debt", section: "corporate-bonds", type: "daily-reports" } });
                                    B.render(dailyReportsFuture, B.findOne('#cr_debt_cb_daily_Future'));

                                    dailyReports = ReportCard({ cardStyle: { class: 'row col-12' }, data: respJSON.CurrentDay || [], info: { name: "debt", section: "corporate-bonds", type: "daily-reports" } });
                                    B.render(dailyReports, B.findOne('#cr_debt_cb_daily_Current'));

                                    dailyReportsPrev = ReportCard({ cardStyle: { class: 'row col-12' }, data: respJSON.PreviousDay || [], info: { name: "debt", section: "corporate-bonds", type: "daily-reports" } });
                                    B.render(dailyReportsPrev, B.findOne('#cr_debt_cb_daily_Previous'));
                                    break;
                                case "TRI-PARTY":
                                    $('#cr_debt_triparty_currentDate').text(respJSON.currentDate || '');
                                    dailyReports = ReportCard({ cardStyle: { class: 'row col-12' }, data: respJSON.CurrentDay || [], info: { name: "debt", section: "triparty", type: "daily-reports" } });
                                    B.render(dailyReports, B.findOne('#cr_debt_triparty_daily_Current'));

                                    break;
                            }
                            chkReports();
                        });
                    });
                }
            });
        });
    };
    getAllMarketStatus();

    var monthlySymbol = ["CM", "INDICES", "SLBS", "FO", "CD", "COM", "IRD", "WDM", "CBM"];
    monthlySymbol.forEach(function (name) {
        B.get('/api/monthly-reports?key=' + name).then(function (resp) {
            var respJSON = [];
            if (resp !== "") {
                respJSON = JSON.parse(resp);
            }
            var monthlyReports = void 0;
            switch (name) {
                case "CM":
                    monthlyReports = ReportCard({ cardStyle: { class: 'row col-12' }, data: respJSON || [], info: { name: "capital-market", section: "equities", type: "monthly-reports" } });
                    B.render(monthlyReports, B.findOne('#cr_equity_monthly_report'));
                    break;
                case "INDICES":
                    monthlyReports = ReportCard({ cardStyle: { class: 'row col-12' }, data: respJSON || [], info: { name: "capital-market", section: "indices", type: "monthly-reports" } });
                    B.render(monthlyReports, B.findOne('#cr_indices_monthly_report'));
                    break;
                case "SLBS":
                    monthlyReports = ReportCard({ cardStyle: { class: 'row col-12' }, data: respJSON || [], info: { name: "capital-market", section: "slb", type: "monthly-reports" } });
                    B.render(monthlyReports, B.findOne('#cr_ssbs_monthly_report'));
                    break;
                case "FO":
                    monthlyReports = ReportCard({ cardStyle: { class: 'row col-12' }, data: respJSON || [], info: { name: "derivatives", section: "equity", type: "monthly-reports" } });
                    B.render(monthlyReports, B.findOne('#cr_deriv_equity_monthly_report'));
                    break;
                case "CD":
                    monthlyReports = ReportCard({ cardStyle: { class: 'row col-12' }, data: respJSON || [], info: { name: "derivatives", section: "currency", type: "monthly-reports" } });
                    B.render(monthlyReports, B.findOne('#cr_derv_currency_monthly_report'));
                    break;
                case "COM":
                    monthlyReports = ReportCard({ cardStyle: { class: 'row col-12' }, data: respJSON || [], info: { name: "derivatives", section: "commodity", type: "monthly-reports" } });
                    B.render(monthlyReports, B.findOne('#cr_derv_commodity_monthly_report'));
                    break;
                case "IRD":
                    monthlyReports = ReportCard({ cardStyle: { class: 'row col-12' }, data: respJSON || [], info: { name: "derivatives", section: "irf", type: "monthly-reports" } });
                    B.render(monthlyReports, B.findOne('#cr_derv_irf_monthly_report'));
                    break;
                case "WDM":
                    monthlyReports = ReportCard({ cardStyle: { class: 'row col-12' }, data: respJSON || [], info: { name: "debt", section: "debt-segment", type: "monthly-reports" } });
                    B.render(monthlyReports, B.findOne('#cr_debt_segment_monthly_report'));
                    break;
                case "CBM":
                    monthlyReports = ReportCard({ cardStyle: { class: 'row col-12' }, data: respJSON || [], info: { name: "debt", section: "corporate-bonds", type: "monthly-reports" } });
                    B.render(monthlyReports, B.findOne('#cr_debt_cb_monthly_report'));
                    break;
            }
        });
    });

    /* start datepicker */
    var today = new Date(new Date().getFullYear(), new Date().getMonth(), new Date().getDate());
    $('.dtpicker').each(function () {
        $(this).datepicker({
            uiLibrary: 'bootstrap4',
            iconsLibrary: 'fontawesome',
            format: 'dd-mmm-yyyy',
            maxDate: new Date(),
            labelMonthNext: 'Go to the next month',
            labelMonthPrev: 'Go to the previous month',
            labelMonthSelect: 'Pick a month from the dropdown',
            labelYearSelect: 'Pick a year from the dropdown',
            selectMonths: true,
            selectYears: true
        });
    });
    /* check uncheck */
    $(".check_uncheck").change(function () {
        var _this = $(this);
        _this.closest('.row').parent('.report_container').find('.reportsDownload').each(function () {
            if (!$(this).hasClass('hide')) {
                $(this).find('input:checkbox').prop("checked", _this.is(':checked'));
            }
        });
        if (_this.is(":checked")) {
            _this.parent().attr('aria-checked', true);
        } else {
            _this.parent().attr('aria-checked', false);
        }
        //$(".checkrow input:checkbox").prop("checked",$(this).is(':checked'));
    });
    $(".checkrow input:checkbox").change(function () {
        if ($(this).prop("checked") == false) {
            $(".check_uncheck").prop("checked", false);
        }
    });
    /* end check uncheck */
    /* tabs to remove active on click on accordion link */
    $('.common_accordion .card-header .card-link').click(function () {
        $('.nav-tabs--vertical .nav-link').removeClass('active');
    });
    /* tabs to remove active on click on accordion link */

    //$('#capital-market').on('click touchstart','.fa-star, .fa-star-o',function(){
    $('#capital-market').on('click touchstart', '.fav', function () {
        addFav($(this).find('.fa-star, .fa-star-o'), favReport, "favCapital");
    });

    $('#reports-derivatives').on('click', '.fav', function () {
        addFav($(this).find('.fa-star, .fa-star-o'), derivativeFavReport, "favDerivatives");
    });

    //$('#reports-debt').on('click','.fa-star, .fa-star-o',function(){
    $('#reports-debt').on('click', '.fav', function () {
        addFav($(this).find('.fa-star, .fa-star-o'), debtFavReport, "favDebt");
    });

    /*$(document).on('click', '#capitalFav .fa-star, #capitalFav .fa-star-o',function(){
        const obj = {"name":$(this).parents('.card').find('label.chk_container').text().trim(), "type":$(this).parents('.reportsDownload').data("type"), "category":$(this).parents('.reportsDownload').data("cat"), "section":$(this).parents('.reportsDownload').data("section")};
        const chkObj = containsObject(obj, favReport);
        favReport.splice(chkObj, 1);
        favReport.splice(chkObj, 1);
        $(this).removeClass('fa-star').addClass("fa-star-o");
        localStorage.setItem("favReportCaiptal", JSON.stringify(favReport));
        checkFav(favReport, '#cr_equity_daily');
          investorEquity("favReportCaiptal", "#QLEquityMarket");
        investorEquity("favReportCaiptal", "#capitalFav");
        $('.capitalEquityCnt').html(favReport.length);
    });*/

    var todayDate = new Date();
    $('.reportTodaysDate').html(dateFormat(todayDate));
});

function containsObject(obj, list) {
    var duplicate = -1;
    list.map(function (item, index) {
        if (JSON.stringify(item) === JSON.stringify(obj)) {
            duplicate = index;
        }
    });
    return duplicate;
}

function checkFav(data, id) {
    try {
        $(id + ' .fa-star').addClass('fa-star-o').removeClass("fa-star");
        if (data.length > 0) {
            $('#capitalFavFilter').show();
            $(id + ' .reportsDownload').each(function () {
                var _this = $(this);
                if ($(this).data('type') === "daily-reports") {
                    data.map(function (item) {
                        /*if(_this.data('link') === item.link){
                            _this.find('.fa').removeClass('fa-star-o').addClass("fa-star");
                        }*/
                        if (_this.find('.chk_container').text().trim() === item.name) {
                            _this.find('.fa').removeClass('fa-star-o').addClass("fa-star");
                        }
                    });
                }
            });
        } else {
            console.log("data", data);
            $('#capitalFavFilter').hide();
        }
    } catch (e) {
        console.log("checkFav", e.message);
    }
}

function filterReports(val, id) {
    try {
        $(id + ' .col-lg-4').removeClass('hide');
        $(id + ' .col-lg-4').each(function () {
            var reportText = $(this).find('.chk_container').text().trim().toLowerCase();
            if (reportText.indexOf(val.toLowerCase()) >= 0) {
                $(this).removeClass('hide');
            } else {
                $(this).addClass('hide');
            }
        });
    } catch (e) {
        console.log("filterReports", e.message);
    }
}
function addFav(_this, data, name) {
    try {
        _this.removeClass('fa-star-o').addClass("fa-star");
        var obj = { "name": _this.parents('.card').find('label.chk_container').text().trim(), "type": _this.parents('.reportsDownload').data("type"), "category": _this.parents('.reportsDownload').data("cat"), "section": _this.parents('.reportsDownload').data("section"), "link": _this.parents('.reportsDownload').data("link") };
        var chkObj = containsObject(obj, data);
        //console.log(chkObj, obj, data)
        if (chkObj >= 0) {
            data.splice(chkObj, 1);
            _this.removeClass('fa-star').addClass("fa-star-o");
        } else {
            if (data.length === 9) {
                alert("Maximum 9 Reports can be Favorites");
                return false;
            }
            data.push(obj);
        }
        localStorage.setItem(name, JSON.stringify(data));

        switch (name) {
            case "favCapital":
                checkFav(data, '#capital-market');
                investorEquity(name, "#QLEquityMarket");
                investorEquity(name, "#capitalFav");
                $('.capitalEquityCnt').html(data.length);
                break;
            case "favDerivatives":
                checkFav(data, '#reports-derivatives');
                investorEquity(name, "#QLDerivativeMarket");
                investorEquity(name, "#derivativeFav");
                $('.derivativeEquityCnt').html(data.length);
                break;
            case "favDebt":
                checkFav(data, '#reports-debt');
                investorEquity(name, "#QLDebtMarket");
                investorEquity(name, "#debtFav");
                $('.debtEquityCnt').html(data.length);
                break;
        }

        //console.log(data)
    } catch (e) {
        console.log("addFav", e.message);
    }
}

function chkReports() {
    try {
        favReport = localStorage.getItem('favCapital') || [];
        favReport = favReport !== null && favReport.length > 0 ? JSON.parse(favReport) : [];

        derivativeFavReport = localStorage.getItem('favDerivatives') || [];
        derivativeFavReport = derivativeFavReport !== null && derivativeFavReport.length > 0 ? JSON.parse(derivativeFavReport) : [];

        debtFavReport = localStorage.getItem('favDebt') || [];
        debtFavReport = debtFavReport !== null && debtFavReport.length > 0 ? JSON.parse(debtFavReport) : [];

        $('.capitalEquityCnt').html(favReport.length);
        $('.derivativeEquityCnt').html(derivativeFavReport.length);
        $('.debtEquityCnt').html(debtFavReport.length);
        //const chkFavStorage = localStorage.getItem(name);
        //const chkFav = chkFavStorage !== null && chkFavStorage.length > 0
        if (favReport !== null) {
            // checkFav(favReport, '#capital-market');
            investorEquity("favCapital", "#capitalFav");
        }
        if (derivativeFavReport !== null) {
            // checkFav(derivativeFavReport, '#reports-derivatives');
            investorEquity("favDerivatives", "#derivativeFav");
        }
        if (debtFavReport !== null) {
            // checkFav(debtFavReport, '#reports-debt');
            investorEquity("favDebt", "#debtFav");
        }
    } catch (e) {
        console.log(e);
    }
}