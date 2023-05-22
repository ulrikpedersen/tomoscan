TOP=../..
include $(TOP)/configure/CONFIG

DB += $(patsubst ../%, %, $(wildcard ../*.template))
DB += $(patsubst ../%, %, $(wildcard ../*.db))
DB += $(patsubst ../%.vdb, %.db, $(wildcard ../*.vdb))

%.d: ;

# flatten any vdb files
$(COMMON_DIR)/%.db: ../%.vdb
	@echo "Flattening $< to produce $@ " 
	flatdb.sh --disable-macro-warnings $< $@	

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE
