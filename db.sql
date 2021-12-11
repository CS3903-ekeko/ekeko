--(){ :; }; exec psql ekekodb -f "$0"

CREATE TABLE trader(
	id BIGSERIAL PRIMARY KEY
);

CREATE TABLE market(
	stock    TEXT,
	currency TEXT,
	PRIMARY  KEY(stock, currency)
);

CREATE TABLE buy_sell_order(
	id          BIGSERIAL PRIMARY KEY,
	trader_id   BIGSERIAL REFERENCES trader(id),
	buy_or_sell BOOLEAN,
	stock       TEXT,
	currency    TEXT,
	price       MONEY,
	amount      DOUBLE PRECISION,
	FOREIGN     KEY (stock, currency) REFERENCES market (stock, currency)
);
