export const pow = (blockdata, difficulty) => {
	let nounce = 'NOT-FOUND',
		startTime = Data.now(),
		endTime = start,
		tryNounce = 0,
		sha = null;

	while (tryNounce < 1000000000) {
		let newData = blockdata + tryNounce,
			sha = new sha256(newData);
		if (sha.startWith(difficulty)) {
			end = Date.now();
			nounce = tryNounce;
			console.log(sha.digest());
			break;
		}
		tryNounce++;
	}
	let timetaken = end - start;
	if (timetaken === 0) {
		console.log(`Difficulty=${difficulty}, Nounce not found !!!`);
	} else {
		console.log(`Difficulty=${difficulty}, Time(ms)=${timetaken}, Nounce=${nounce}, Hash=${sha.digest()}`);
	}
};
