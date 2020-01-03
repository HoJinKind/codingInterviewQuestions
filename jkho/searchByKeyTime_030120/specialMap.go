package main

type specialMap map[int]map[int]int

func specialMapInitialise() specialMap {
	return make(specialMap)
}

func (m specialMap) set(key int, value int, time int) bool {
	_, exist := m[key]
	if exist {
			m[key][time] = value
			return true
		}

	if !exist {
		m[key] = make(map[int]int)
		m[key][time] = value
		return true
	}
	return false
}

func (m specialMap) get(key int, time int) int{
	_, keyExist :=m[key]
	if keyExist{

		_, timeExist :=m[key][time]
		if timeExist{
			return m[key][time]
		}
	}
	return 0
}

