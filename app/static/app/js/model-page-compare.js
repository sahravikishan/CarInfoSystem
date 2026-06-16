(function () {
    "use strict";

    var MAX_TOTAL = 4;

    function normalizePath(path) {
        if (!path) return "/";
        return path.endsWith("/") ? path : path + "/";
    }

    function toNumber(value) {
        if (!value || value === "--") return null;
        var match = String(value).match(/([0-9]+(?:\.[0-9]+)?)/);
        if (!match) return null;
        var n = Number(match[1]);
        return Number.isFinite(n) ? n : null;
    }

    function priceToRupees(value) {
        if (!value || value === "--") return null;

        var txt = String(value).replace(/,/g, " ");
        var parts = txt.match(/([0-9]+(?:\.[0-9]+)?)\s*(cr|crore|lakh)?/i);
        if (!parts) return null;

        var base = Number(parts[1]);
        if (!Number.isFinite(base)) return null;

        var unit = (parts[2] || "").toLowerCase();
        if (unit === "cr" || unit === "crore") return base * 10000000;
        if (unit === "lakh") return base * 100000;

        return base;
    }

    function injectStyles() {
        if (document.getElementById("model-segment-compare-styles")) return;

        var style = document.createElement("style");
        style.id = "model-segment-compare-styles";
        style.textContent = [
            ".msc-trigger {",
            "  position: fixed;",
            "  right: 18px;",
            "  bottom: 18px;",
            "  z-index: 1090;",
            "  border: 1px solid rgba(226, 226, 224, 0.28);",
            "  border-radius: 999px;",
            "  background: linear-gradient(135deg, #12484C, #0E2931);",
            "  color: #FFFFFF;",
            "  padding: 11px 16px;",
            "  font: inherit;",
            "  font-size: 0.84rem;",
            "  font-weight: 700;",
            "  letter-spacing: 0.02em;",
            "  cursor: pointer;",
            "  box-shadow: 0 14px 28px rgba(0, 0, 0, 0.3);",
            "}",
            ".msc-trigger:hover { filter: brightness(1.08); }",

            ".msc-overlay {",
            "  position: fixed;",
            "  inset: 0;",
            "  z-index: 1200;",
            "  background: rgba(4, 14, 18, 0.68);",
            "  display: none;",
            "  align-items: center;",
            "  justify-content: center;",
            "  padding: 14px;",
            "}",
            ".msc-overlay.is-open { display: flex; }",

            ".msc-modal {",
            "  width: min(1120px, 100%);",
            "  max-height: min(88vh, 920px);",
            "  overflow: auto;",
            "  border-radius: 16px;",
            "  border: 1px solid rgba(226, 226, 224, 0.2);",
            "  background: linear-gradient(155deg, rgba(14, 41, 49, 0.98), rgba(18, 72, 76, 0.95));",
            "  color: #E2E2E0;",
            "  box-shadow: 0 24px 58px rgba(0, 0, 0, 0.45);",
            "}",
            ".msc-head {",
            "  display: flex;",
            "  justify-content: space-between;",
            "  gap: 12px;",
            "  align-items: center;",
            "  padding: 14px 16px;",
            "  border-bottom: 1px solid rgba(226, 226, 224, 0.14);",
            "}",
            ".msc-head h3 { margin: 0; font-size: 1.05rem; color: #FFFFFF; }",
            ".msc-head p { margin: 4px 0 0; font-size: 0.82rem; color: rgba(226, 226, 224, 0.86); }",
            ".msc-close {",
            "  border: none;",
            "  background: transparent;",
            "  color: #E2E2E0;",
            "  padding: 8px 10px;",
            "  font: inherit;",
            "  cursor: pointer;",
            "  font-size: 1.4rem;",
            "  display: flex;",
            "  align-items: center;",
            "  justify-content: center;",
            "  transition: all 0.2s ease;",
            "  border-radius: 8px;",
            "}",
            ".msc-close:hover {",
            "  color: #ff6b6b;",
            "  background: rgba(220, 53, 69, 0.15);",
            "}",
            ".msc-tabs {",
            "  display: flex;",
            "  align-items: center;",
            "  gap: 4px;",
            "  padding: 10px 16px;",
            "  border-bottom: 1px solid rgba(226, 226, 224, 0.14);",
            "  background: rgba(14, 41, 49, 0.5);",
            "}",
            ".msc-tab-spacer { flex: 1; }",
            ".msc-tab-btn {",
            "  background: transparent;",
            "  border: none;",
            "  color: rgba(226, 226, 224, 0.66);",
            "  padding: 8px 14px;",
            "  border-radius: 8px;",
            "  cursor: pointer;",
            "  font: inherit;",
            "  font-size: 0.82rem;",
            "  font-weight: 600;",
            "  display: flex;",
            "  gap: 6px;",
            "  align-items: center;",
            "  transition: all 0.2s ease;",
            "}",
            ".msc-tab-btn:hover { color: #FFFFFF; background: rgba(18, 72, 76, 0.3); }",
            ".msc-tab-btn.is-active {",
            "  background: rgba(18, 72, 76, 0.8);",
            "  color: #FFFFFF;",
            "  border-bottom: 2px solid #2B7574;",
            "}",
            ".msc-clear-btn {",
            "  background: rgba(220, 53, 69, 0.2);",
            "  border: 1px solid rgba(220, 53, 69, 0.4);",
            "  color: #ff6b6b;",
            "  padding: 8px 12px;",
            "  border-radius: 8px;",
            "  cursor: pointer;",
            "  font: inherit;",
            "  font-size: 0.78rem;",
            "  font-weight: 600;",
            "  display: flex;",
            "  gap: 5px;",
            "  align-items: center;",
            "  transition: all 0.2s ease;",
            "}",
            ".msc-clear-btn:hover {",
            "  background: rgba(220, 53, 69, 0.35);",
            "  border-color: rgba(220, 53, 69, 0.6);",
            "}",
            ".msc-tab-content { display: none; }",
            ".msc-tab-content.is-active { display: grid; gap: 14px; }",
            ".msc-body {",
            "  padding: 14px 16px 16px;",
            "  display: grid;",
            "  gap: 14px;",
            "}",
            ".msc-controls { display: grid; grid-template-columns: 1fr auto; gap: 10px; align-items: center; }",
            ".msc-search, .msc-search-custom {",
            "  border: 1px solid rgba(226, 226, 224, 0.22);",
            "  border-radius: 10px;",
            "  background: rgba(14, 41, 49, 0.82);",
            "  color: #FFFFFF;",
            "  padding: 9px 11px;",
            "  font: inherit;",
            "}",
            ".msc-search::placeholder, .msc-search-custom::placeholder { color: rgba(226, 226, 224, 0.6); }",
            ".msc-summary, .msc-summary-custom { font-size: 0.82rem; color: rgba(226, 226, 224, 0.86); }",

            ".msc-cars, .msc-cars-custom {",
            "  display: grid;",
            "  grid-template-columns: repeat(auto-fill, minmax(210px, 1fr));",
            "  gap: 10px;",
            "}",
            ".msc-card {",
            "  border: 1px solid rgba(226, 226, 224, 0.14);",
            "  border-radius: 10px;",
            "  padding: 10px;",
            "  background: rgba(14, 41, 49, 0.72);",
            "  display: grid;",
            "  gap: 7px;",
            "}",
            ".msc-card.is-current { border-color: rgba(226, 226, 224, 0.45); background: rgba(18, 72, 76, 0.76); }",
            ".msc-title { margin: 0; color: #FFFFFF; font-size: 0.88rem; font-weight: 700; }",
            ".msc-meta { margin: 0; color: rgba(226, 226, 224, 0.82); font-size: 0.77rem; }",
            ".msc-check { display: inline-flex; align-items: center; gap: 6px; font-size: 0.78rem; color: #E2E2E0; }",
            ".msc-check input { accent-color: #2B7574; }",

            ".msc-table-wrap { overflow: auto; border: 1px solid rgba(226, 226, 224, 0.14); border-radius: 10px; }",
            ".msc-table { width: 100%; min-width: 700px; border-collapse: collapse; }",
            ".msc-table th, .msc-table td {",
            "  border-bottom: 1px solid rgba(226, 226, 224, 0.12);",
            "  padding: 9px 11px;",
            "  text-align: left;",
            "  vertical-align: top;",
            "  font-size: 0.8rem;",
            "}",
            ".msc-table thead th {",
            "  background: rgba(18, 72, 76, 0.95);",
            "  color: #FFFFFF;",
            "  font-size: 0.76rem;",
            "  letter-spacing: 0.04em;",
            "  text-transform: uppercase;",
            "}",
            ".msc-table td { color: rgba(226, 226, 224, 0.9); }",
            ".msc-table td.metric { color: #FFFFFF; font-weight: 700; min-width: 180px; }",
            ".msc-table td.best { background: rgba(43, 117, 116, 0.3); color: #FFFFFF; font-weight: 800; }",
            ".msc-note { font-size: 0.76rem; color: rgba(226, 226, 224, 0.74); }",

            "@media (max-width: 820px) {",
            "  .msc-trigger { right: 12px; bottom: 12px; padding: 10px 13px; font-size: 0.75rem; }",
            "  .msc-controls { grid-template-columns: 1fr; }",
            "  .msc-tabs { flex-wrap: wrap; gap: 6px; }",
            "  .msc-tab-spacer { width: 100%; }",
            "  .msc-clear-btn { padding: 6px 10px; font-size: 0.72rem; }",
            "  .msc-modal { max-height: min(95vh, 100vh); }",
            "}",
            ".msc-toast {",
            "  position: fixed;",
            "  bottom: 20px;",
            "  right: 20px;",
            "  z-index: 1500;",
            "  background: linear-gradient(155deg, rgba(220, 53, 69, 0.95), rgba(185, 28, 28, 0.95));",
            "  color: #FFFFFF;",
            "  padding: 14px 18px;",
            "  border-radius: 10px;",
            "  border-left: 4px solid #ff6b6b;",
            "  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);",
            "  font-size: 0.9rem;",
            "  font-weight: 600;",
            "  display: flex;",
            "  align-items: center;",
            "  gap: 10px;",
            "  max-width: 400px;",
            "  animation: slideInToast 0.3s ease forwards;",
            "}",
            "@keyframes slideInToast {",
            "  from { opacity: 0; transform: translateX(400px); }",
            "  to { opacity: 1; transform: translateX(0); }",
            "}",
            ".msc-toast.is-exit {",
            "  animation: slideOutToast 0.3s ease forwards;",
            "}",
            "@keyframes slideOutToast {",
            "  from { opacity: 1; transform: translateX(0); }",
            "  to { opacity: 0; transform: translateX(400px); }",
            "}",
            ".msc-toast i {",
            "  flex-shrink: 0;",
            "  font-size: 1.1rem;",
            "}",
            "@media (max-width: 640px) {",
            "  .msc-toast {",
            "    bottom: 12px;",
            "    right: 12px;",
            "    left: 12px;",
            "    max-width: none;",
            "  }",
            "}",
            "@media (prefers-reduced-motion: reduce) {",
            "  .msc-trigger, .msc-modal, .msc-toast { transition: none !important; animation: none !important; }",
            "}"
        ].join("\n");

        document.head.appendChild(style);
    }

    function getBestIndices(cars, metric) {
        if (metric.rule === "text") return [];

        var values = cars.map(function (car) {
            var raw = car[metric.key];
            if (metric.rule === "min-price") return priceToRupees(raw);
            return toNumber(raw);
        });

        var valid = values.filter(function (v) { return v !== null; });
        if (!valid.length) return [];

        var best = metric.rule === "min-price" ? Math.min.apply(null, valid) : Math.max.apply(null, valid);
        var out = [];

        values.forEach(function (v, i) {
            if (v !== null && v === best) out.push(i);
        });

        return out;
    }

    function buildTableHtml(cars) {
        var metrics = [
            { key: "brand", label: "Brand", rule: "text" },
            { key: "segment", label: "Segment", rule: "text" },
            { key: "body_type", label: "Body Type", rule: "text" },
            { key: "price", label: "Starting Price", rule: "min-price" },
            { key: "on_road", label: "On-road (Starting)", rule: "min-price" },
            { key: "fuel", label: "Fuel Type", rule: "text" },
            { key: "transmission", label: "Transmission", rule: "text" },
            { key: "mileage", label: "Mileage", rule: "max-num" },
            { key: "power", label: "Power", rule: "max-num" },
            { key: "seats", label: "Seats", rule: "max-num" }
        ];

        var thead = "<thead><tr><th>Metric</th>" +
            cars.map(function (car) { return "<th>" + car.name + "</th>"; }).join("") +
            "</tr></thead>";

        var rows = metrics.map(function (metric) {
            var best = getBestIndices(cars, metric);
            var values = cars.map(function (car, idx) {
                var cls = best.indexOf(idx) !== -1 ? " class=\"best\"" : "";
                return "<td" + cls + ">" + (car[metric.key] || "--") + "</td>";
            }).join("");
            return "<tr><td class=\"metric\">" + metric.label + "</td>" + values + "</tr>";
        }).join("");

        return thead + "<tbody>" + rows + "</tbody>";
    }

    function init() {
        var data = Array.isArray(window.CIS_CAR_COMPARE_DATA) ? window.CIS_CAR_COMPARE_DATA : [];
        if (!data.length) return;

        var path = normalizePath(window.location.pathname || "/");
        if (path.indexOf("_full_detail/") === -1) return;

        var current = data.find(function (car) {
            return normalizePath(car.url || "") === path;
        });

        if (!current) return;

        var segment = current.segment || "Car";
        var sameSegment = data.filter(function (car) {
            return (car.segment || "Car") === segment;
        });

        if (sameSegment.length <= 1) return;

        injectStyles();

        function showNotification(message) {
            var existing = document.querySelector(".msc-toast");
            if (existing) existing.remove();

            var toast = document.createElement("div");
            toast.className = "msc-toast";
            toast.innerHTML = "<i class=\"fas fa-exclamation-circle\"></i><span>" + message + "</span>";
            document.body.appendChild(toast);

            setTimeout(function () {
                toast.classList.add("is-exit");
                setTimeout(function () { toast.remove(); }, 300);
            }, 3500);
        }

        // Get competitors from different brands, max 7
        var allPeers = sameSegment.filter(function (car) {
            return car.id !== current.id;
        });

        var brandsToShow = {};
        var recommendedPeers = [];
        var currentBrand = current.brand;

        for (var i = 0; i < allPeers.length; i++) {
            var peer = allPeers[i];
            var peerBrand = peer.brand || "Other";
            if (peerBrand !== currentBrand && !brandsToShow[peerBrand]) {
                brandsToShow[peerBrand] = true;
                recommendedPeers.push(peer);
                if (Object.keys(brandsToShow).length >= 7) break;
            }
        }

        var peers = recommendedPeers;

        var state = {
            query: "",
            queryCustom: "",
            selectedPeerIds: peers.slice(0, Math.max(0, MAX_TOTAL - 1)).map(function (x) { return x.id; }),
            currentTab: "recommended"
        };

        var trigger = document.createElement("button");
        trigger.type = "button";
        trigger.className = "msc-trigger";
        trigger.innerHTML = "<i class=\"fas fa-scale-balanced\"></i> Compare";

        var overlay = document.createElement("div");
        overlay.className = "msc-overlay";
        overlay.innerHTML = [
            "<div class=\"msc-modal\" role=\"dialog\" aria-modal=\"true\" aria-label=\"Compare cars\">",
            "  <div class=\"msc-head\">",
            "    <div>",
            "      <h3>Compare Cars</h3>",
            "      <p>Current model: <strong>" + current.name + "</strong>. Select up to " + MAX_TOTAL + " cars total.</p>",
            "    </div>",
            "    <button type=\"button\" class=\"msc-close\" data-msc-close><i class=\"fas fa-times-circle\"></i></button>",
            "  </div>",
            "  <div class=\"msc-tabs\">",
            "    <button type=\"button\" class=\"msc-tab-btn is-active\" data-msc-tab=\"recommended\"><i class=\"fas fa-star\"></i> Recommended</button>",
            "    <button type=\"button\" class=\"msc-tab-btn\" data-msc-tab=\"custom\"><i class=\"fas fa-search-plus\"></i> Custom Compare</button>",
            "    <div class=\"msc-tab-spacer\"></div>",
            "    <button type=\"button\" class=\"msc-clear-btn\" data-msc-clear><i class=\"fas fa-trash-alt\"></i> Clear</button>",
            "  </div>",
            "  <div class=\"msc-body\">",
            "    <div class=\"msc-tab-content is-active\" data-msc-tab-content=\"recommended\">",
            "      <div class=\"msc-controls\">",
            "        <input type=\"search\" class=\"msc-search\" data-msc-search placeholder=\"Search brand or car name...\">",
            "        <div class=\"msc-summary\" data-msc-summary></div>",
            "      </div>",
            "      <div class=\"msc-cars\" data-msc-cars></div>",
            "    </div>",
            "    <div class=\"msc-tab-content\" data-msc-tab-content=\"custom\">",
            "      <div class=\"msc-controls\">",
            "        <input type=\"search\" class=\"msc-search-custom\" data-msc-search-custom placeholder=\"Search car, brand, or segment (e.g., Sedan, SUV, BMW)...\">",
            "        <div class=\"msc-summary-custom\" data-msc-summary-custom></div>",
            "      </div>",
            "      <div class=\"msc-cars-custom\" data-msc-cars-custom></div>",
            "    </div>",
            "    <div class=\"msc-table-wrap\"><table class=\"msc-table\" data-msc-table></table></div>",
            "    <div class=\"msc-note\">Best values are highlighted. Select up to " + MAX_TOTAL + " cars to compare.</div>",
            "  </div>",
            "</div>"
        ].join("");

        document.body.appendChild(trigger);
        document.body.appendChild(overlay);

        var closeBtn = overlay.querySelector("[data-msc-close]");
        var clearBtn = overlay.querySelector("[data-msc-clear]");
        var searchInput = overlay.querySelector("[data-msc-search]");
        var searchInputCustom = overlay.querySelector("[data-msc-search-custom]");
        var summaryEl = overlay.querySelector("[data-msc-summary]");
        var summaryElCustom = overlay.querySelector("[data-msc-summary-custom]");
        var carsEl = overlay.querySelector("[data-msc-cars]");
        var carsElCustom = overlay.querySelector("[data-msc-cars-custom]");
        var tableEl = overlay.querySelector("[data-msc-table]");
        var tabBtns = overlay.querySelectorAll("[data-msc-tab]");
        var tabContents = overlay.querySelectorAll("[data-msc-tab-content]");

        function selectedCars() {
            var selectedPeers = data.filter(function (p) {
                return state.selectedPeerIds.indexOf(p.id) !== -1;
            });
            return [current].concat(selectedPeers);
        }

        function filteredPeers() {
            var q = (searchInput.value || "").toLowerCase().trim();
            if (!q) return peers;
            return peers.filter(function (car) {
                var txt = [car.name, car.brand, car.body_type, car.fuel].join(" ").toLowerCase();
                return txt.indexOf(q) !== -1;
            });
        }

        function filteredCustom() {
            var q = (searchInputCustom.value || "").toLowerCase().trim();
            if (!q) return data.filter(function (car) { return car.id !== current.id; });
            return data.filter(function (car) {
                if (car.id === current.id) return false;
                var txt = [car.name, car.brand, car.segment, car.body_type].join(" ").toLowerCase();
                return txt.indexOf(q) !== -1;
            });
        }

        function renderPeerCards() {
            var filtered = filteredPeers();
            summaryEl.textContent = filtered.length + " cars available";

            var currentCard = [
                "<article class=\"msc-card is-current\">",
                "  <p class=\"msc-title\">" + current.name + "</p>",
                "  <p class=\"msc-meta\">Current Model | " + current.brand + "</p>",
                "  <p class=\"msc-meta\"><a class=\"compare-tag\" href=\"" + current.url + "\">Open Detail</a></p>",
                "</article>"
            ].join("");

            var peerCards = filtered.map(function (car) {
                var checked = state.selectedPeerIds.indexOf(car.id) !== -1 ? " checked" : "";
                return [
                    "<article class=\"msc-card\">",
                    "  <p class=\"msc-title\">" + car.name + "</p>",
                    "  <p class=\"msc-meta\">" + car.brand + " | " + car.price + "</p>",
                    "  <label class=\"msc-check\">",
                    "    <input type=\"checkbox\" data-msc-toggle=\"" + car.id + "\"" + checked + "> Add",
                    "  </label>",
                    "</article>"
                ].join("");
            }).join("");

            carsEl.innerHTML = currentCard + peerCards;

            carsEl.querySelectorAll("[data-msc-toggle]").forEach(function (input) {
                input.addEventListener("change", function () {
                    var id = input.getAttribute("data-msc-toggle");
                    var idx = state.selectedPeerIds.indexOf(id);

                    if (input.checked) {
                        if (idx === -1) {
                            if ((state.selectedPeerIds.length + 1) >= MAX_TOTAL) {
                                showNotification("You can compare up to " + MAX_TOTAL + " cars including the current model.");
                                input.checked = false;
                                return;
                            }
                            state.selectedPeerIds.push(id);
                        }
                    } else if (idx >= 0) {
                        state.selectedPeerIds.splice(idx, 1);
                    }

                    renderTable();
                });
            });
        }

        function renderCustomCards() {
            var filtered = filteredCustom();
            var displayLimit = searchInputCustom.value ? 999 : 20; // Show all when searching
            var displayed = filtered.slice(0, displayLimit);
            
            summaryElCustom.textContent = filtered.length + " cars available" + (filtered.length > displayLimit ? " (" + displayLimit + " shown)" : "");

            var currentCard = [
                "<article class=\"msc-card is-current\">",
                "  <p class=\"msc-title\">" + current.name + "</p>",
                "  <p class=\"msc-meta\">Current Model | " + current.brand + "</p>",
                "</article>"
            ].join("");

            if (displayed.length === 0 && searchInputCustom.value) {
                carsElCustom.innerHTML = currentCard + "<p style=\"grid-column: 1/-1; text-align: center; color: rgba(226, 226, 224, 0.6); padding: 20px;\">No cars found. Try a different search.</p>";
                return;
            }

            var customCards = displayed.map(function (car) {
                var checked = state.selectedPeerIds.indexOf(car.id) !== -1 ? " checked" : "";
                return [
                    "<article class=\"msc-card\">",
                    "  <p class=\"msc-title\">" + car.name + "</p>",
                    "  <p class=\"msc-meta\">" + car.brand + " | " + car.segment + "</p>",
                    "  <p class=\"msc-meta\" style=\"color: rgba(226, 226, 224, 0.66);\">" + car.price + "</p>",
                    "  <label class=\"msc-check\">",
                    "    <input type=\"checkbox\" data-msc-toggle-custom=\"" + car.id + "\"" + checked + "> Add",
                    "  </label>",
                    "</article>"
                ].join("");
            }).join("");

            carsElCustom.innerHTML = currentCard + customCards;

            carsElCustom.querySelectorAll("[data-msc-toggle-custom]").forEach(function (input) {
                input.addEventListener("change", function () {
                    var id = input.getAttribute("data-msc-toggle-custom");
                    var idx = state.selectedPeerIds.indexOf(id);

                    if (input.checked) {
                        if (idx === -1) {
                            if ((state.selectedPeerIds.length + 1) >= MAX_TOTAL) {
                                showNotification("You can compare up to " + MAX_TOTAL + " cars including the current model.");
                                input.checked = false;
                                return;
                            }
                            state.selectedPeerIds.push(id);
                        }
                    } else if (idx >= 0) {
                        state.selectedPeerIds.splice(idx, 1);
                    }

                    renderTable();
                });
            });
        }

        function renderTable() {
            var cars = selectedCars();
            if (cars.length <= 1) {
                tableEl.innerHTML = "<tr><td colspan=\"2\" style=\"padding: 30px; text-align: center; color: rgba(226, 226, 224, 0.6);\">Select cars to compare. Use the Recommended or Custom Compare tabs above.</td></tr>";
                return;
            }
            tableEl.innerHTML = buildTableHtml(cars);
        }

        function openModal() {
            overlay.classList.add("is-open");
            renderPeerCards();
            renderCustomCards();
            renderTable();
        }

        function closeModal() {
            overlay.classList.remove("is-open");
        }

        function switchTab(tabName) {
            state.currentTab = tabName;
            tabBtns.forEach(function (btn) {
                if (btn.getAttribute("data-msc-tab") === tabName) {
                    btn.classList.add("is-active");
                } else {
                    btn.classList.remove("is-active");
                }
            });
            tabContents.forEach(function (content) {
                if (content.getAttribute("data-msc-tab-content") === tabName) {
                    content.classList.add("is-active");
                    if (tabName === "recommended") searchInput.focus();
                    if (tabName === "custom") searchInputCustom.focus();
                } else {
                    content.classList.remove("is-active");
                }
            });
        }

        trigger.addEventListener("click", openModal);
        closeBtn.addEventListener("click", closeModal);

        clearBtn.addEventListener("click", function () {
            state.selectedPeerIds = [];
            renderPeerCards();
            renderCustomCards();
            renderTable();
        });

        tabBtns.forEach(function (btn) {
            btn.addEventListener("click", function () {
                var tabName = btn.getAttribute("data-msc-tab");
                switchTab(tabName);
            });
        });

        overlay.addEventListener("click", function (event) {
            if (event.target === overlay) closeModal();
        });

        searchInput.addEventListener("input", function () {
            renderPeerCards();
        });

        searchInputCustom.addEventListener("input", function () {
            renderCustomCards();
        });

        document.addEventListener("keydown", function (event) {
            if (event.key === "Escape" && overlay.classList.contains("is-open")) {
                closeModal();
            }
        });
    }

    document.addEventListener("DOMContentLoaded", init);
})();
