import M5
import asyncio

from hardware import sdcard


def setup():
    M5.begin()
    # init SDCard
    sdcard.SDCard(slot=3, width=1, sck=40, miso=39, mosi=14, cs=12, freq=20000000)
    # init speaker
    M5.Speaker.config(
        buzzer=False,
        pin_data_out=46,  # Serial data line of I2S, representing audio data in binary complement. ASDOUT on ES8311
        pin_bck=41,  # Serial clock line of I2S, corresponding to each bit of digital audio data.
        pin_ws=43,  # Frame clock of I2S, used to switch left and right channel data.
        sample_rate=48000,  # 22050,
        stereo=True,
        dma_buf_len=256,
        dma_buf_count=8,
        task_priority=5,
        task_pinned_core=1,
        i2s_port=0,
        use_dac=False,
    )
    M5.Speaker.begin()
    M5.Speaker.tone(4000, 50)
    M5.Speaker.playWavFile("/sd/Mp3/")
    # M5.Speaker.playWavFile("/system/common/wav/bg.wav")
    # Speaker.setVolumePercentage(50)

    # asyncio.create_task(coro=loop())
    # asyncio.sleep_ms(10)∏∏


async def loop() -> None:
    M5.update()
    # kb.kb.tick()
    M5.Speaker.playWavFile("/system/common/wav/bg.wav")
    await asyncio.sleep_ms(200)


if __name__ == "__main__":
    try:
        setup()
        asyncio.run(loop())
    except (asyncio.CancelledError, KeyboardInterrupt) as e:
        from utility import print_error_msg

        print_error_msg(e)
    except ImportError:
        print("please update to latest firmware")
    finally:
        pass
